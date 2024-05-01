import Test.HUnit
import Solucion

main = runTestTT tests


tests = test [
    "personaConMasAmigos 1 elemento" ~: pertenece_hunit (personaConMasAmigos validas1) (aplanar_hunit validas1) ~?= True,
    "personaConMasAmigos empate" ~: pertenece_hunit (personaConMasAmigos validas2) (aplanar_hunit validas2) ~?= True,
    "personaConMasAmigos" ~: pertenece_hunit (personaConMasAmigos validas3) (aplanar_hunit validas3) ~?= True,
    "personaConMasAmigos2" ~: personaConMasAmigos validas4 ~?= "A"
    ]

--Formulas

pertenece_hunit :: (Eq t) => t -> [t] -> Bool
pertenece_hunit _ [] = False
pertenece_hunit x (y:ys) | x == y = True
                   | otherwise = pertenece_hunit x ys

aplanar_hunit :: [(t, t)] -> [t]
aplanar_hunit [] = []
aplanar_hunit ((a, b):xs) = a:(b:(aplanar_hunit xs))


--Listas

validas1 = [("X", "Z")]
validas2 = [("X", "Z"), ("P", "Q"), ("A", "B")]
validas3 = [("X", "Z"), ("P", "Q"), ("A", "B"), ("X", "A"), ("Z", "A")]
validas4 = [("A", "B"), ("X", "A"), ("Z", "A"), ("X", "Z"), ("P", "Q")]
