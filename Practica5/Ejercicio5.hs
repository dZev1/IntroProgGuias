-- 1
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [t] = [t]
sumaacumulada (x:xs) = x : sumaacumulada ((head (xs) + x) : tail xs)

-- 2
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = descomponerEnFactoresPrimosDesde 2 x  : descomponerEnPrimos xs

descomponerEnFactoresPrimosDesde :: Integer -> Integer -> [Integer]
descomponerEnFactoresPrimosDesde 2 1 = []
descomponerEnFactoresPrimosDesde n m | esDivisible m n = n : descomponerEnFactoresPrimosDesde 2 (div m n)
                                     | otherwise = descomponerEnFactoresPrimosDesde (siguientePrimo n) m


siguientePrimo :: Integer -> Integer
siguientePrimo n | esPrimo (n + 1) = n + 1
                 | otherwise = siguientePrimo (n + 1)

menorDivisor :: Integer -> Integer
menorDivisor = menorDivisorDesde 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde m n | mod n m == 0 = m
                      | otherwise = menorDivisorDesde (m + 1) n

esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

esDivisible :: Integer -> Integer -> Bool
esDivisible n m = mod n m == 0