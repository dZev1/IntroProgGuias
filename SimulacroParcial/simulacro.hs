module Simulacro where

-- RELACIONES VALIDAS
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((usr1,usr2):xs) | usr1 == usr2 = False
                                   | pertenece (usr1,usr2) xs || pertenece (usr2,usr1) xs = False
                                   | otherwise = relacionesValidas xs

-- Agrego funcion pertenece, que revisa si hay una tupla igual en la lista de tuplas
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece t (x:xs) = t == x || pertenece t xs

-------------------------------------------------------------------------------------

-- PERSONAS
personas :: [(String, String)] -> [String]
personas [] = []
personas ((usr1,usr2):xs) | usr1 /= usr2 = eliminarRepetidos (usr1: usr2 : personas xs)
                          | otherwise = personas xs

-- Agrego funcion eliminarRepetidos, que toma una lista y quita los elementos que se repiten
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [t] = [t]
eliminarRepetidos (x:xs) | pertenece x xs = [] ++ eliminarRepetidos xs
                         | otherwise = x : eliminarRepetidos xs

-------------------------------------------------------------------------------------

-- AMIGOS DE
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe usr ((x,y):xs) | usr == x =  y : amigosDe usr xs
                        | usr == y =  x : amigosDe usr xs
                        | otherwise = amigosDe usr xs

-------------------------------------------------------------------------------------

-- PERSONA CON MAS AMIGOS
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos ((x,y):xs) = x

-- Agrego funciones auxiliares
-- Cuenta CUANTAS veces aparece un determinado string en una lista
contar :: String -> [(String, String)] -> Integer
contar _ [] = 0
contar t ((x,y):xs) | perteneceAUX t [(x,y)] = 1 + contar t xs
                    | otherwise = contar t xs

maximo :: [Integer] -> Integer
maximo [n] = n
maximo (x:xs) | x >= maximo xs = x
              | otherwise = maximo xs

-- Funcion Pertenece pero tweakeada para que acepte string -> tupla de strings
perteneceAUX :: (Eq t) => t -> [(t,t)] -> Bool
perteneceAUX _ [] = False
perteneceAUX t ((x,y):xs) = t == x || t == y || perteneceAUX t xs



