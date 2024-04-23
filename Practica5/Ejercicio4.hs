type Texto = [Char]

-- a
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [t] = [t]
sacarBlancosRepetidos (x:y:xs) | x == y && x == ' ' = x : sacarBlancosRepetidos xs
                               | otherwise = x : sacarBlancosRepetidos (y:xs)

-- b
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras [t] = 1
contarPalabras xs = contarEspacios (limpiarCadena xs) + 1   

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x == ' ' = 1 + contarEspacios xs
                      | otherwise = contarEspacios xs

sacarEspacioFinal :: [Char] -> [Char]
sacarEspacioFinal [] = []
sacarEspacioFinal (x:[]) | x == ' ' = []
                         | otherwise = [x]
sacarEspacioFinal (x:xs) = x:sacarEspacioFinal xs

sacarEspacioInicio :: [Char] -> [Char]
sacarEspacioInicio [] = []
sacarEspacioInicio (x:xs) | x == ' ' = xs
                          | otherwise = x:xs

limpiarCadena :: [Char] -> [Char]
limpiarCadena xs = sacarEspacioInicio (sacarEspacioFinal (sacarBlancosRepetidos xs))

-- c
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras xs = primeraPalabra xs : palabras (sacarPrimeraPalabra (limpiarCadena xs))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x ==' ' =[]
                      | otherwise = x:primeraPalabra xs

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] =[]
sacarPrimeraPalabra (x:xs) | x==' ' = xs
                           | otherwise = sacarPrimeraPalabra xs

-- d

