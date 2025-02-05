(define (square n) (* n n))

(define (pow base exp) 'YOUR-CODE-HERE)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let (
               (y 
                  (repeatedly-cube (- n 1) x))
              )
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
