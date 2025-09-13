;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "notes-lecture-VirTheo"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("graphicx" "") ("longtable" "") ("wrapfig" "") ("rotating" "") ("ulem" "normalem") ("amsmath" "") ("amssymb" "") ("capt-of" "") ("hyperref" "") ("geometry" "left=25mm" "right=25mm" "top=25mm" "bottom=25mm")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "inputenc"
    "fontenc"
    "graphicx"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "amssymb"
    "capt-of"
    "hyperref"
    "geometry")
   (LaTeX-add-labels
    "sec:org9ea376e"
    "sec:org701fab5"
    "eq:first_moment_second_law"
    "sec:orgc7f92cb"
    "sec:orgf9cd74f"
    "eq:HSE"
    "eq:pot"
    "eq:vir"
    "eq:second_thermodynamics_law"
    "eq:virial_star"
    "sec:orgb900a6b"
    "sec:org490d5de"
    "sec:orgcd8542a"
    "eq:tau_KH"
    "eq:KH_timescale_scaling"
    "sec:orgceacfdc"
    "sec:org5f8286b"))
 :latex)

