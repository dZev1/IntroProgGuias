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
laQueMasHayQueCodificar frase mapeo = laQueMasHayQueCodificarAuxiliar frase frase mapeo

laQueMasHayQueCodificarAuxiliar :: [Char] -> [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificarAuxiliar [t] _ _ = t
laQueMasHayQueCodificarAuxiliar (l1:l2:ls) frase mapeo
    | cuantasVecesHayQueCodificar l1 frase mapeo >= cuantasVecesHayQueCodificar l2 frase mapeo = laQueMasHayQueCodificarAuxiliar (l1:ls) frase mapeo
    | otherwise = laQueMasHayQueCodificarAuxiliar (l2:ls) frase mapeo

-- Ejercicio 4
codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase (l:fs) mapeo
    | hayQueCodificar l mapeo = obtenerReemplazo l mapeo : codificarFrase fs mapeo
    | otherwise = l : codificarFrase fs mapeo

obtenerReemplazo :: Char -> [(Char, Char)] -> Char
obtenerReemplazo c ((a,r):xs)
    | c == a = r
    | otherwise = obtenerReemplazo c xs