maximo :: [Integer] -> Integer
maximo [x] = x
--maximo (x:xs) | x >= maximo xs = x
--              | otherwise = maximo xs

maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar ns = ordenar (quitar (maximo ns) ns) ++ [maximo ns]


quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (t:ts) | x == t = ts
                | otherwise = t : quitar x ts