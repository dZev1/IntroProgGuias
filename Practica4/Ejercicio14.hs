-- 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = (potencias q n) * (potencias q m)

potencias :: Integer -> Integer -> Integer
potencias q 1 = q
potencias q n = potencias q (n - 1) * (q ^ n)

-- 16
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorHasta n

menorDivisorHasta n 
