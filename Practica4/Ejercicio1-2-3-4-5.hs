-- Implementar la funcion fibonacci:: Integer -> Integer que devuelve el i-esimo numero de Fibonacci. Recordar que la secuencia de Fibonacci se define como:
-- fib(0) = 0
-- fib(1) = 1
-- fib(n+2) = fib(n-1) + fib(n)
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

-- Implementar una funcion parteEntera :: Float -> Integer segun la siguiente especificacion:
-- problema parteEntera (x: R) : Z {
--   requiere: { True }
--   asegura: { resultado ≤ x < resultado + 1 }
-- }
parteEntera :: Float -> Integer
parteEntera n | n < (-1) && n < 0  = -1 --NO ES NECESARIA ESTA LINEA -> parteEntera -0.34 = parteEntera 0.35 - 1 = -1 
              | 0 <= n && n < 1 = 0
              | n >= 1 = 1 + parteEntera (n - 1)
              | otherwise = (-1) + parteEntera (n + 1)

-- Especificar e implementar la funcion esDivisible :: Integer -> Integer -> Bool que dados dos numeros naturales
-- determina si el primero es divisible por el segundo. No esta permitido utilizar las funciones mod ni div.
esDivisible :: Integer -> Integer -> Bool 
esDivisible n m | n == 0 = True
                | n < 0 = False
                | otherwise = esDivisible (n - m) m

-- Especificar e implementar la funcion sumaImpares :: Integer -> Integer que dado n ∈ N sume los primeros n numeros impares.
-- Por ejemplo: sumaImpares 3 => 1+3+5 => 9.
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = (2 * n - 1) + sumaImpares (n - 1)

-- Implementar la funcion medioFact :: Integer -> Integer que dado n ∈ N calcula n!! = n (n−2)(n−4)· · ·
-- problema medioFac (n: Z) : Z {
--  requiere: { n ≥ 0 }
--  asegura: { resultado = \prod_{i=0}^{floor{frac{n-1}{2}} \left(n-2i \right) }
-- }

medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact(n - 2)