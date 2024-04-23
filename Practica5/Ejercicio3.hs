-- maximo :: [Integer] -> Integer segun la siguiente especificacion:
-- problema maximo (s: seq⟨Z⟩) : Z {
--  requiere: { |s| > 0 }
-- asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
-- }

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x
              | otherwise = maximo xs

--maximo (x:y:xs) | x >= y = maximo (x:xs)
--                | otherwise = maximo (y:xs)

-- ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente.
-- Sugerencia: Pensar como pueden usar la funcion maximo para que ayude a generar la lista ordenada necesaria.
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar ns = ordenar (quitar (maximo ns) ns) ++ [maximo ns]


quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (t:ts) | x == t = ts
                | otherwise = t : quitar x ts