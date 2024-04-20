-- longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos.
longitud :: [t] -> Integer
longitud [] = 0
longitud ts = 1 + longitud (tail ts)

-- ultimo :: [t] -> t segun la siguiente especificacion:
-- problema ultimo (s: seq⟨T⟩) : T {
--  requiere: { |s| > 0 }
--  asegura: { resultado = s[|s| − 1] }
-- }

ultimo :: [t] -> t
ultimo [t] = t 
ultimo (t:ts) | longitud ts == 0 = t
              | otherwise = ultimo ts

-- principio :: [t] -> [t] segun la siguiente especificacion:
-- problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
--  requiere: { |s| > 0 }
--  asegura: { resultado = subseq(s, 0, |s| − 1) }
-- }

principio :: [t] -> [t]
principio [] = []
principio (t:ts) | longitud ts /= 0 = t:principio ts
                 | longitud ts == 0 = principio []


-- reverso :: [t] -> [t] segun la siguiente especificacion:
-- problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
--  requiere: { True }
--  asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
-- }

reverso :: [t] -> [t]
reverso [] = []
reverso [t] = [t]
reverso (x:xs) = reverso xs ++ [x]