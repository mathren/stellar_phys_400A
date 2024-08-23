;; modified from https://systemcrafters.net/publishing-websites-with-org-mode/building-the-site/

;; Set the package installation directory so that packages aren't stored in the
;; ~/.emacs.d/elpa path.
(require 'package)
(setq package-user-dir (expand-file-name "./.packages"))
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("elpa" . "https://elpa.gnu.org/packages/")))

;; Initialize the package system
(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

;; Install dependencies
(package-install 'htmlize)

;; Load the publishing system
(require 'ox-publish)


(defun mr/get-modified-org-files ()
  "Return a list of Org files modified since the last commit."
  (let* ((default-directory (expand-file-name "./org-content"))
         (modified-files (split-string (shell-command-to-string "git diff --name-only HEAD -- *.org") "\n" t)))
    (mapcar (lambda (file) (expand-file-name file default-directory)) modified-files)))

(defun mr/check-for-all-flag-and-publish ()
  "Check if all is in the command-line arguments."
  (if (member "all" command-line-args)
      (org-publish-all t) ;; publish all
    (let ((modified-files (mr/get-modified-org-files)))
      (if modified-files
	  (org-publish-project "org-site:main")
	(message "No modified Org files found.")))
    ))



(defun mr/read-file (file)
  "Read contents of FILE to string"
  (with-temp-buffer (insert-file-contents file) (buffer-string)))

(defconst mr/site-html-head
  (mr/read-file "html-content/html-templates/html_head.html"))

(defconst mr/site-html-preamble
  (mr/read-file "html-content/html-templates/preamble.html"))

(defconst mr/html-postamble
  (format (mr/read-file "html-content/html-templates/postamble.html")
	  (format-time-string "%-d %B %Y")
	  emacs-version
	  org-version
	  ))

;; fix timestamps for html and latex exports
(defun mr/filter-timestamp (trans back _comm)
  "Remove <> around time-stamps."
  (pcase back
    (`html
     (replace-regexp-in-string "&[lg]t;" "" trans))
    (`latex
     (replace-regexp-in-string "[<>]" "" trans))))

;; fix export of Sun symbol
(defun mr/export-odot-html (backend)
  "Custom filter to replace LaTeX \odot with HTML sun symbol `&#9737;`."
  (when (org-export-derived-backend-p backend 'html)
    (save-excursion
      (goto-char (point-min))
      (while (re-search-forward "\\\\odot" nil t)
        (replace-match "☉" nil t)))))


(add-hook 'org-export-before-processing-hook 'mr/export-odot-html)
(add-to-list 'org-export-filter-timestamp-functions
             #'mr/filter-timestamp)

;; Customize the HTML output
(setq org-html-validation-link nil            ;; Don't show validation link
      org-html-head-include-scripts nil       ;; Use our own scripts
      org-html-head-include-default-style nil ;; Use our own styles
      user-full-name "Mathieu Renzo"          ;; for creator
      org-html-head mr/site-html-head
      org-html-preamble mr/site-html-preamble
      org-html-postamble mr/html-postamble
      org-display-custom-times t
      )



;; define the publishing project
(setq org-publish-project-alist
      (list
       (list "org-site:main"
             :base-directory "./org-content"
	     :publishing-directory "./html-content"
	     :recursive t
	     :exclude "LICENSE\\|\\.gitignore"
             :publishing-function 'org-html-publish-to-html
	     :html-doctype "html5"
	     :language "en"
	     :html-html5-fancy t
	     :email "mrenzo@arizona.edu"
	     :meta-type "website"
	     :description: "Website for 400A Theoretical Astrophysics - Stellar Evolution"
	     :with-title nil
	     :with-latex t
	     :with-sub-superscript t
	     :with-tags t
	     :with-tasks t
	     :html-self-link-headlines nil
             :with-timestamps t					;; Include time stamp in file
             :with-toc nil					;; Don't include a table of contents
             :section-numbers nil				;; Don't include section numbers
             :file-list (mr/get-modified-org-files)		;; Use the list of modified files only
	     )))

;; Generate the site output
(mr/check-for-all-flag-and-publish)
(message "Build complete!")
