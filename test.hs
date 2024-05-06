import Distribution.PackageDescription.FieldGrammar (formatExtraSourceFiles)
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