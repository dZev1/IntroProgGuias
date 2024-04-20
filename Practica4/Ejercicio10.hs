-- Especificar, implementar y dar el tipo de las siguientes funciones (simil Ejercicio 4 Practica 2 de Algebra 1)

-- A

f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2^n + f1 (n - 1)

-- B
f2 :: Integer -> Integer -> Integer
f2 n 1 = n
f2 1 q = q^1
f2 n q = q^n + f2 (n - 1) q

-- C
f3 :: Integer -> Integer -> Integer
f3 n 1 = 2 * n
f3 1 q = f2 2 q
f3 n q = f2 (2 * n) q

-- D
f4 :: Integer -> Integer -> Integer
f4 n q = f3 n q - f2 (n - 1) q