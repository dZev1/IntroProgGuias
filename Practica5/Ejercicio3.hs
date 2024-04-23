-- sumatoria :: [Integer] -> Integer que sume cada uno de los numeros de cada posición de la lista

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- productoria :: [Integer] -> Integer que multiplique cada uno de los numeros de cada posición de la lista
productoria :: [Integer] -> Integer
productoria [] = 0
productoria [t] = t
productoria (x:xs) = x * productoria xs

-- maximo :: [Integer] -> Integer segun la siguiente especificacion:
-- problema maximo (s: seq⟨Z⟩) : Z {
--  requiere: { |s| > 0 }
-- asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
-- }

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x
              | otherwise = maximo xs

--maximo (x:y:xs) | x >= y = maximo (x:xs)
--                | otherwise = maximo (y:xs)

-- sumarN :: Integer -> [Integer] -> [Integer]:
-- problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
-- requiere: { True }
-- asegura: {|resultado| = |s| ∧ cada posicion de resultado contiene el valor que hay en esa posicion en s sumado n }
-- }
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (x + n) : sumarN n xs

-- sumarElPrimero :: [Integer] -> [Integer]
-- problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
--  requiere: { |s| > 0 }
--  asegura: {resultado = sumarN (s[0], s)}
-- }
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- sumarElUltimo :: [Integer] -> [Integer] segun la siguiente especificacion:
-- problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
--  requiere: { |s| > 0 }
--  asegura: {resultado = sumarN (s[|s| − 1], s) }
-- }
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo xs = sumarN (head (reverso xs)) xs

reverso :: [t] -> [t]
reverso [] = []
reverso [t] = [t]
reverso (x:xs) = reverso xs ++ [x]

-- pares :: [Integer] -> [Integer] que devuelve una lista con todos los elementos pares de s, en el orden dado,
-- respetando repeticiones.
pares :: [Integer] -> [Integer]
pares [] = []
pares (t:ts) | mod t 2 == 0 = t : pares ts
             | otherwise = pares ts

-- multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un numero n y una lista xs,
-- devuelve una lista con los elementos de xs multiplos de n.
multiplosDeN n [] = []
multiplosDeN n (x:xs) | esMultiploDe x n = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe n m | mod n m == 0 = True
                 | mod n m /= 0 = False

-- ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente.
-- Sugerencia: Pensar como pueden usar la funcion maximo para que ayude a generar la lista ordenada necesaria.
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar ns = ordenar (quitar (maximo ns) ns) ++ [maximo ns]


quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (t:ts) | x == t = ts
                | otherwise = t : quitar x ts
