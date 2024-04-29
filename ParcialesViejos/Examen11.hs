-- Ejercicio 1
votosEnBlanco :: [(String, String)] -> [Integer] -> Integer -> Integer
votosEnBlanco _ votosPositivos cantTotalVotos = cantTotalVotos - contarVotosPositivos votosPositivos

contarVotosPositivos :: [Integer] -> Integer
contarVotosPositivos [] = 0
contarVotosPositivos (y:ys) = y + contarVotosPositivos ys

-- Ejercicio 2
formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas ((presidente,vicepresidente):xs) | presidente == vicepresidente = False
                                                 | estaContenido (presidente, vicepresidente) xs = False
                                                 | otherwise = formulasValidas xs

estaContenido :: (String, String) -> [(String, String)] -> Bool
estaContenido _ [] = False
estaContenido (v1,v2) ((x1,x2):xs) | v1 == x1 || v1 == x2 || estaContenido (v1,v2) xs = True
                                   | v2 == x1 || v2 == x2 || estaContenido (v1,v2) xs = True
                                   | otherwise = estaContenido (v1, v2) xs

-- Ejercicio 3
porcentajeDeVotos :: String -> [(String, String)] -> [Integer] -> Float
porcentajeDeVotos presidente formulas votos = division (cantidadDeVotos presidente formulas votos * 100) (contarVotosPositivos votos)


cantidadDeVotos :: String -> [(String, String)] -> [Integer] -> Integer
cantidadDeVotos _ [] _ = 0
cantidadDeVotos _ _ [] = 0
cantidadDeVotos presidente ((candidato,vice):xs) (y:ys) | presidente == candidato = y
                                                        | otherwise = cantidadDeVotos presidente xs ys

division :: Integer -> Integer -> Float
division n m = fromIntegral n / fromIntegral m

-- Ejercicio 4
proximoPresidente :: [(String, String)] -> [Integer] -> String
proximoPresidente formulas votos = proximoPresidenteAux formulas formulas votos

proximoPresidenteAux :: [(String, String)] -> [(String, String)] -> [Integer] -> String
proximoPresidenteAux [] _ _ = ""
proximoPresidenteAux ((candidato,vice):[]) _ _ = candidato
proximoPresidenteAux ((c1,v1):(c2,v2):xs) formulas votos | votosCandidato1 >= votosCandidato2 = proximoPresidenteAux ((c1,v1):xs) formulas votos
                                                         | otherwise = proximoPresidenteAux ((c2,v2):xs) formulas votos
                                                        where
                                                            votosCandidato1 = cantidadDeVotos c1 formulas votos
                                                            votosCandidato2 = cantidadDeVotos c2 formulas votos