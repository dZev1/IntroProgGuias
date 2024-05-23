import Data.Char
--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

devolverElementoEnPosicion :: [a] -> Integer -> a
devolverElementoEnPosicion (x:xs) n
    | n == 0 = x
    | otherwise = devolverElementoEnPosicion xs (n - 1)

maximo :: [Integer] -> Integer
maximo [] = 0
maximo (x:xs)
    | x >= maximo xs = x
    | otherwise = maximo xs

maximoString :: [String] -> String
maximoString [] = ""
maximoString (xs : xss)
    | length xs > length (maximoString xss) = xs
    | otherwise = maximoString xss

ordenarStrings :: [String] -> [String]
ordenarStrings [] = []
ordenarStrings ts = ordenarStrings (quitar (maximoString ts) ts) ++ [maximoString ts]

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (t:ts)
    | x == t = ts
    | otherwise = t : quitar x ts


listaDePares :: [Int] -> [Int]
listaDePares [] = []
listaDePares (x:xs)
    | mod x 2 == 0 = x : listaDePares xs
    | otherwise = listaDePares xs

devolverCocientes :: [(Int, Int)] -> [Int]
devolverCocientes [] = []
devolverCocientes ((a,b):xs) = div b a : devolverCocientes xs

formarVectores :: [Int] -> [Int] -> [(Int,Int)]
formarVectores [] [] = []
formarVectores (x:xs) (y:ys) = (x,y) : formarVectores xs ys

devolverPosicionesImpares :: [String] -> String
devolverPosicionesImpares [] = ""
devolverPosicionesImpares xs = devolverPosicionesImparesAux (length xs) xs

devolverPosicionesImparesAux :: Int -> [String] -> String
devolverPosicionesImparesAux _ [] = ""
devolverPosicionesImparesAux n (x:xs)
    | mod (n - (n - 1)) 2 /= 0 = x ++ devolverPosicionesImparesAux (length xs) xs
    | otherwise = devolverPosicionesImparesAux (n + 1) xs

esMinuscula :: Char -> Bool
esMinuscula c = ord c >= 97 && ord c <= 122

letraANatural :: Char -> Int
letraANatural c = ord c - ord 'a'

-- Función para contar las ocurrencias de una letra en una cadena
contarLetra :: Char -> String -> Int
contarLetra _ [] = 0
contarLetra c (x:xs)
    | not (esMinuscula c) = 0
    | c == x = 1 + contarLetra c xs
    | otherwise = contarLetra c xs

-- Función para calcular el porcentaje de una letra en una cadena
porcentajeLetra :: Char -> String -> Float
porcentajeLetra letra cadena =
    fromIntegral (contarLetra letra cadena) / fromIntegral (length cadena) * 100

-- Función principal para calcular la frecuencia de cada letra
frecuencia :: String -> [Float]
frecuencia cadena = calcularFrecuencias cadena "abcdefghijklmnopqrstuvwxyz"

calcularFrecuencias :: String -> String -> [Float]
calcularFrecuencias _ [] = []
calcularFrecuencias cadena (letra:resto) = porcentajeLetra letra cadena * fromIntegral (contarLetra letra cadena) : calcularFrecuencias cadena resto

