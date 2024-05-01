module Solucion where

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
personas ((usr1,usr2):xs) | usr1 /= usr2 = eliminarRepetidos (usr1 : usr2 : personas xs)
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
cantidadDeAmigos :: String -> [(String,String)] -> Int
cantidadDeAmigos usr xs = length (amigosDe usr xs)
 

mayorAmigueroAux :: [String]->[(String,String)]->String
mayorAmigueroAux [x] _ = x
mayorAmigueroAux (x:y:xs) relaciones
    | cantidadDeAmigos x relaciones >= cantidadDeAmigos y relaciones = mayorAmigueroAux (x:xs) relaciones
    | otherwise = mayorAmigueroAux (y:xs) relaciones


personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos relaciones = mayorAmigueroAux (personas relaciones) relaciones   
