-- Implementar una funcion: distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1,p2,p3) (q1,q2,q3) = abs (p1 - q1) + abs (p2 - q2) + abs (p3 - q3)
