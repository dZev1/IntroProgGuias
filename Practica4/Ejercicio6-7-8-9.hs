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
                      | otherwise = ultimoDigito n == ultimoDigito (sacarUltimoDigito n) && todosDigitosIguales (sacarUltimoDigito n)

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = div n 10

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
              | otherwise = 1 + cantDigitos(sacarUltimoDigito n)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = ultimoDigito n
                 | otherwise = iesimoDigito (sacarUltimoDigito n) i

-- Especificar e implementar una funcion esCapicua :: Integer -> Bool que dado n ∈ N≥0 determina si n es un numero capicua.
esCapicua :: Integer -> Bool
esCapicua n | todosDigitosIguales n = True
            | esCapicuaAux n = True
            | otherwise = False

esCapicuaAux :: Integer -> Bool
esCapicuaAux n
    | n >= 10 && n <= 99 = todosDigitosIguales n
    | n >= 100 && n < 1000 = ultimoDigito n == primerDigito n
    | otherwise = esCapicuaAux (sacarPrimerDigito(sacarUltimoDigito n))

primerDigito :: Integer -> Integer
primerDigito n
    | n >= 0 && n < 10 = n
    | otherwise = primerDigito (sacarUltimoDigito n)

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n
    | n >= 10 && n < 100 = ultimoDigito n
    | otherwise = mod n (10^(cantDigitos n - 1))
            
