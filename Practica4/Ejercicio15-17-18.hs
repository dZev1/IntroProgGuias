-- Especificar e implementar una funcion sumaRacionales :: Integer -> Integer -> Float que dados dos
-- naturales n, m sume todos los numeros racionales de la forma p/q con 1 ≤ p ≤ n y 1 ≤ q ≤ m, es decir:
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
import GHC.TypeLits (sameChar)
{-# HLINT ignore "Use even" #-}

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

-- Implementar una funcion mayorDigitoPar :: Integer -> Integer segun la siguiente especificacion:
-- problema mayorDigitoPar (n: N) : N {
-- requiere: { True }
-- asegura: { resultado es el mayor de los digitos pares de n. Si n no tiene ningun digito par, entonces resultado es -1. }
-- }
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | n < 10 && esPar n = n
                 | n < 10 && not (esPar n) = -1
                 | esPar (ultimoDigito n) = esMaximo (ultimoDigito n) (mayorDigitoPar (sacarUltimoDigito n))
                 | otherwise = mayorDigitoPar (sacarUltimoDigito n)

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

esMaximo :: Integer -> Integer -> Integer
esMaximo n m | n >= m = n
             | otherwise = m

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = div n 10

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10