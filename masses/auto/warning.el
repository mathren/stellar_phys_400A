(TeX-add-style-hook
 "warning"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("beamer" "xcolor=dvipsnames" "professionalfonts" "aspectratio=169" "fontsize=120pt")))
   (TeX-run-style-hooks
    "latex2e"
    "./setup"
    "beamer"
    "beamer10"))
 :latex)

