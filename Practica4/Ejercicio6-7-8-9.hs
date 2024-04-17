-- Especificar e implementar la funcion sumaDigitos :: Integer -> Integer que calcula la suma de digitos de
-- un numero natural. Para esta funcion pueden utilizar div y mod.
sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

-- Implementar la funcion todosDigitosIguales :: Integer -> Bool que determina si todos los dıgitos de un numero natural son iguales, es decir:
--  problema todosDigitosIguales (n: Z) : Bool {
--      requiere: { n > 0 }
--      asegura: { resultado = true ↔ todos los d´ıgitos de n son iguales }
--  }

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = ultimoDigito n == ultimoDigito (sacaUltimoDigito n) && todosDigitosIguales (sacaUltimoDigito n)

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacaUltimoDigito :: Integer -> Integer
sacaUltimoDigito n = div n 10

-- Implementar la funcion iesimoDigito :: Integer -> Integer -> Integer que dado un n ∈ N≥0 y un i ∈ N menor o igual a la cantidad de digitos de n, devuelve el i-esimo digito de n.
-- problema iesimoDigito (n: Z, i: N) : Z {
--  requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
--  asegura: { resultado = (n div 10^(cantDigitos(n)−i)) mod 10 }
-- }
-- problema cantDigitos (n: Z) : N {
--  requiere: { n ≥ 0 }
--  asegura: { n = 0 → resultado = 1}
--  asegura: { n /= 0 → (n div 10^(resultado−1) > 0 ∧ n div 10^(resultado) = 0) }
-- }

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos(sacaUltimoDigito n)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = ultimoDigito n
                 | otherwise = iesimoDigito (sacaUltimoDigito n) i

-- Especificar e implementar una funcion esCapicua :: Integer -> Bool que dado n ∈ N≥0 determina si n es un numero capicua.
esCapicua :: Integer -> Bool
esCapicua n | n < 10 = True
            
