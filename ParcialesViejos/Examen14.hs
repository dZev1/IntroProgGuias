-- Ejercicio 1
hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar _ [] = False
hayQueCodificar c ((a,b):xs)
    | c == a = True
    | otherwise = hayQueCodificar c xs

-- Ejercicio 2
cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int
cuantasVecesHayQueCodificar c frase mapeo
    | not (hayQueCodificar c mapeo) = 0
    | otherwise = contarCuantasVecesAparece c frase

contarCuantasVecesAparece :: Char -> [Char] -> Int
contarCuantasVecesAparece _ [] = 0
contarCuantasVecesAparece c (x:xs)
    | c == x = 1 + contarCuantasVecesAparece c xs
    | otherwise = contarCuantasVecesAparece c xs

-- Ejercicio 3
laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar [t] _ = t
laQueMasHayQueCodificar (l1:l2:xs) mapeo
    | cuantasVecesHayQueCodificar l1 (l1:l2:xs) mapeo >= cuantasVecesHayQueCodificar l2 (l1:l2:xs) mapeo = laQueMasHayQueCodificar (l1: quitar l2 xs) mapeo
    | otherwise = laQueMasHayQueCodificar (l2: quitar l1 xs) mapeo

quitar :: Char -> [Char] -> [Char]
quitar _ [] = []
quitar n (x:xs)
    | n == x = quitar n xs
    | otherwise = x : quitar n xs

-- Ejercicio 4
codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase (l:ls) mapeo
    | hayQueCodificar l mapeo = reemplazar l mapeo : codificarFrase ls mapeo
    | otherwise = l : codificarFrase ls mapeo

reemplazar :: Char -> [(Char, Char)] -> Char
reemplazar c ((m,r):ms)
    | c == m = r
    | otherwise = reemplazar c ms