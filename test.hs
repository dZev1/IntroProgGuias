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