(defun pr (x)
  (cond ((atom x) (pratom x))
        (t (prlist x))))

(defun pratom (x)
  (format *standard-output* "~a" x))

(defun prrpar () (format *standard-output* ")"))

(defun prspaced (x)
  (format *standard-output* " ")
  (pr x))

(defun prlist (x)
  (format *standard-output* "(")
  (pr (car x))
  (cond ((null (cdr x)) (prrpar))
        ((and (atom (cdr x)) (not (null (cdr x))))
         (format *standard-output* " . ")
         (pr (cdr x))
         (prrpar))
        (t
         (mapc #'prspaced (cdr x))
         (prrpar))))
