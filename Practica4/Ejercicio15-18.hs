-- Especificar e implementar una funcion sumaRacionales :: Integer -> Integer -> Float que dados dos
-- naturales n, m sume todos los numeros racionales de la forma p/q con 1 ≤ p ≤ n y 1 ≤ q ≤ m, es decir:

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = sumaRacionales (n - 1) m + sumaRacionalesInterna n m

sumaRacionalesInterna :: Integer -> Integer -> Float
sumaRacionalesInterna _ 0 = 0
sumaRacionalesInterna n m = fromIntegral n / fromIntegral m + sumaRacionalesInterna n (m - 1) 

-- Implementar la funcion esFibonacci :: Integer -> Bool segun la siguiente especificacion:
-- problema esFibonacci (n: Z) : B {
--  requiere: { n ≥ 0 }
--  asegura: { resultado = true ↔ n es algun valor de la secuencia de Fibonacci definida en el ejercicio 1}

fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

esFibonacci :: Integer -> Bool
esFibonacci 0 = True
esFibonacci 1 = True
esFibonacci n = esFibonacciDesde 1 n

esFibonacciDesde :: Integer -> Integer -> Bool
esFibonacciDesde n 1 = True
esFibonacciDesde n m | fibonacci n == m = True
                     | fibonacci n > m = False
                     | otherwise = esFibonacciDesde (n + 1) m