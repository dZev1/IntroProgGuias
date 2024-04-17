-- 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = (potencias q n) * (potencias q m)

potencias :: Integer -> Integer -> Integer
potencias q 1 = q
potencias q n = potencias q (n - 1) * (q ^ n)

-- 16 a
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde 2 n 

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde m n | mod n m == 0 = m
                      | otherwise = menorDivisorDesde (m + 1) n

-- 16 b
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n