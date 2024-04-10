-- Implementar una funcion: distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1,p2,p3) (q1,q2,q3) = absoluto (p1 - q1) + absoluto (p2 - q2) + absoluto (p3 - q3)

absoluto :: Integer -> Integer
absoluto n | n >= 0 = n
           | n < 0 = -n
