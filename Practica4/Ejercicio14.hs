-- 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = potencias q n * potencias q m

potencias :: Integer -> Integer -> Integer
potencias q 1 = q
potencias q n = potencias q (n - 1) * (q ^ n)

-- 16 a
menorDivisor :: Integer -> Integer
menorDivisor = menorDivisorDesde 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde m n | mod n m == 0 = m
                      | otherwise = menorDivisorDesde (m + 1) n

-- 16 b
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

-- 16 c
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = maximoComunDivisor n m == 1

maximoComunDivisor :: Integer -> Integer -> Integer
maximoComunDivisor n 0 = n
maximoComunDivisor n m = maximoComunDivisor m (mod n m)

-- 16 d
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = siguientePrimo (nEsimoPrimo (n - 1))

siguientePrimo :: Integer -> Integer
siguientePrimo n | esPrimo (n + 1) = n + 1
                 | otherwise = siguientePrimo (n + 1)