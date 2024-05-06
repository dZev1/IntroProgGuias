module Solucion2 where
-- FUNCIONES AUXILIARES VARIAS
perteneceTupla :: (String, String) -> [(String, String)] -> Bool
perteneceTupla _ [] = False
perteneceTupla (p1,p2) ((l1,l2):ls)
    | p1 == l1 || p1 == l2 = True
    | p2 == l1 || p2 == l2 = True
    | otherwise = perteneceTupla (p1, p2) ls

perteneceString :: (Eq t) => t -> [t] -> Bool
perteneceString _ [] = False
perteneceString x (y:ys)
    | x == y = True
    | otherwise = perteneceString x ys

longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs


-- EJERCICIO 1
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((p1,p2):xs)
    | p1 == p2 = False
    | perteneceTupla (p1,p2) xs = False
    | otherwise = relacionesValidas xs


-- EJERCICIO 2
personas :: [(String, String)] -> [String]
personas [] = []
personas xs = eliminarRepetidos (aplanar xs)

aplanar :: [(String, String)] -> [String]
aplanar [] = []
aplanar ((x,y):xs) = x:y:aplanar xs

eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [] = []
eliminarRepetidos [t] = [t]
eliminarRepetidos (x:xs)
    | perteneceString x xs = eliminarRepetidos xs
    | otherwise = x : eliminarRepetidos xs


-- EJERCICIO 3
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((usr1,usr2):usrs)
    | persona == usr1 = usr2 : amigosDe persona usrs
    | persona == usr2 = usr1 : amigosDe persona usrs
    | otherwise = amigosDe persona usrs


-- EJERCICIO 4
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos relaciones = tieneMasAmigos (personas relaciones) relaciones

cantidadDeAmigos :: String -> [(String, String)] -> Int
cantidadDeAmigos p ps = longitud (amigosDe p ps)

tieneMasAmigos :: [String] -> [(String, String)] -> String
tieneMasAmigos [t] _ = t
tieneMasAmigos (x:y:xs) relaciones
    | cantidadDeAmigos x relaciones > cantidadDeAmigos y relaciones = tieneMasAmigos (x:xs) relaciones
    | otherwise = tieneMasAmigos (y:xs) relaciones