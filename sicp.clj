(ns sicp)

(defn fast-exp-iter [x power]
  (loop [a 1
	 b x
	 n power]
    (cond (= n 1) (* a b)
	  (even? n) (recur a (* b b) (/ n 2))
	  :else (recur (* a b) (* b b) (/ (- n 1) 2)))))
