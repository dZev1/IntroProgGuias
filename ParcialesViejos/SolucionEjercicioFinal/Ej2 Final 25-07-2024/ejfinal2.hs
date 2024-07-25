maximo :: [Int] -> Int
maximo [x] = x 
maximo (y:x:xs) | y >= x = maximo (y:xs)
                | otherwise = maximo (x:xs)

subsecuencia :: Int -> [Int] -> [Int]
subsecuencia 0 _ = []
subsecuencia _ [] = []
subsecuencia n (x:xs) = x : subsecuencia (n - 1) xs

maximoPorSubsecuencia :: [Int] -> [Int] -> [Int]
maximoPorSubsecuencia [] _ = []
maximoPorSubsecuencia (x:xs) ys = maximo (subsecuencia (x + 1) ys) : maximoPorSubsecuencia xs ys