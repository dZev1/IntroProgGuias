-- Implementar una funcion estanRelacionados :: Integer -> Integer -> Bool
-- requiere: {a ̸= 0 ∧ b ̸= 0}
-- asegura: {(res = true) <-> a ∗ a + a ∗ b ∗ k = 0 para algun k ∈ Z con k ̸= 0)}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b | mod (abs a) (abs b) == 0 = True
                      | mod (abs a) (abs b) /= 0 = False