module Examen13 where
-- Division
division :: Int -> Int -> Float
division n m = fromIntegral n / fromIntegral m

-- Ejercicio 1

golesDeNoGoleadores :: [(String, String)] -> [Int] -> Int -> Int
golesDeNoGoleadores _ golesDeGoleadoreSs totalGoles = totalGoles - contarGolesDeGoleadores golesDeGoleadoreSs

contarGolesDeGoleadores :: [Int] -> Int
contarGolesDeGoleadores [] = 0
contarGolesDeGoleadores (x:xs) = x + contarGolesDeGoleadores xs

-- Ejercicio 2
equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos (eJ:xs) 
    | pertenece eJ xs = False
    | otherwise = equiposValidos xs

pertenece :: (String, String) -> [(String,String)] -> Bool
pertenece _ [] = False
pertenece (e1,j1) ((e2,j2):xs)
    | e1 == j2 || e1 == e2 = True
    | e2 == j2 || e2 == j2 = True
    | otherwise = pertenece (e1, j1) xs

-- Ejercicio 3
porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles jugador eqJuGs goles = division ((calcularGolesDe jugador eqJuGs goles) * 100) (contarGolesDeGoleadores goles)

calcularGolesDe :: String -> [(String, String)] -> [Int] -> Int
calcularGolesDe jugador ((eq,jg):xs) (goles:ys)
    | jugador == jg = goles
    | otherwise = calcularGolesDe jugador xs ys

-- Ejercicio 4
botinDeOro :: [(String, String)] -> [Int] -> String
botinDeOro eqJuGs goles = devolverJugadorCon (maximo goles) eqJuGs goles

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:xs)
    | x > maximo xs = x
    | otherwise = maximo xs

devolverJugadorCon :: Int -> [(String, String)] -> [Int] -> String
devolverJugadorCon x ((e,j):xs) (y:ys)
    | x == y = j 
    | otherwise = devolverJugadorCon x xs ys