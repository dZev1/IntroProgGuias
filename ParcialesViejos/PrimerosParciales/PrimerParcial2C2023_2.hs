division :: Int -> Int -> Float
division n m = fromIntegral n / fromIntegral m

-- Ejercicio 1
porcentajeDeVotosAfirmativos :: [(String, String)] -> [Int] -> Int  -> Float
porcentajeDeVotosAfirmativos _ votos cantVotos = division ((totalVotosAfirmativos votos) * 100) cantVotos

totalVotosAfirmativos :: [Int] -> Int
totalVotosAfirmativos [] = 0
totalVotosAfirmativos (x:xs) = x + totalVotosAfirmativos xs


-- Ejercicio 2
formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas ((candidato,vice):xs) 
    | candidato == vice = True
    | pertenece (candidato,vice) xs = True
    | otherwise = formulasInvalidas xs

pertenece :: (String,String) -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece (c1,v1) ((c2,v2):xs)
    | c1 == c2 || c1 == v2 = True
    | c2 == v1 || c2 == v2 = True
    | otherwise = pertenece (c1,v1) xs
                            

-- Ejercicio 3
porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos _ [] [] = 0
porcentajeDeVotos nombreVice listas votos = division ((votosDe nombreVice listas votos) * 100) (totalVotosAfirmativos votos) 

votosDe :: String -> [(String,String)] -> [Int] -> Int
votosDe _ [] [] = 0
votosDe nombreVice ((presi,vice):xs) (y:ys)
    | nombreVice == vice = y 
    | otherwise = votosDe nombreVice xs ys

-- Ejercicio 4
menosVotado :: [(String, String)] -> [Int] -> String
menosVotado [(x,y)] _ = x
menosVotado ((candidato,vice):xs) (y:ys)
    | minimo (y:ys) == y = candidato
    | otherwise = menosVotado xs ys

minimo :: [Int] -> Int
minimo [x] = x
minimo (x:xs)
    | x <= minimo xs = x
    | otherwise = minimo xs