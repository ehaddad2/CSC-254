(defun fill-triangle (n k)
  (if (or (= k 0) (= k n))
      1
    (+ (fill-triangle (1- n) (1- k))
       (fill-triangle (1- n) k))))

(defun print-row (r i)
  (when (<= i r)
    (princ (fill-triangle r i))
    (princ " ")
    (print-row r (1+ i))))

(defun print-triangle (n i)
  (when (< i n)
    (print-row i 0)
    (format t "~%")  
    (print-triangle n (1+ i))))
    
(defun main (argv)
  (let ((n (parse-integer (first argv))))
    (print-triangle n 0))) 

(main (cdr *posix-argv*))