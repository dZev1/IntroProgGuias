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


desplazar :: Char -> Int -> Char
desplazar c n | not (esMinuscula c) = c
              | otherwise = chr (ord 'a' + mod (letraANatural c + n) 26)

cifrar :: String -> Int -> String
cifrar [] _ = []
cifrar (x:xs) n = desplazar x n : cifrar xs n

cifrarLista :: [String] -> [String]
cifrarLista [] = []
cifrarLista (x:xs) = cifrarLista (quitarUltimoString (x:xs)) ++ [cifrar (ultimoString (x:xs)) (posicion (ultimoString (x:xs)) (x:xs))]

-- esta función auxiliar me indica el número de la posición del string en la lista, siendo la primer posición correspondiente al número 0
posicion :: String -> [String] -> Int
posicion x (y:ys) | length (y:ys) == 1 = 0
                  | x == y = 0
                  | otherwise = 1 + posicion x ys

-- esta función auxiliar devuelve el último string de una lista de string
ultimoString :: [String] -> String
ultimoString [] = []
ultimoString (x:xs) | length(x:xs) == 1 = x
                    | otherwise = ultimoString xs    

-- esta función auxiliar quita el último string de una lista de string
quitarUltimoString :: [String] -> [String]
quitarUltimoString [] = []
quitarUltimoString (x:xs) | length(x:xs) == 1 = []
                          | otherwise = [x] ++ quitarUltimoString xs     
