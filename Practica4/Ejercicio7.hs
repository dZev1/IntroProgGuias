-- Implementar la funcion todosDigitosIguales :: Integer -> Bool que determina si todos los dıgitos de un numero natural son iguales, es decir:
--  problema todosDigitosIguales (n: Z) : Bool {
--      requiere: { n > 0 }
--      asegura: { resultado = true ↔ todos los d´ıgitos de n son iguales }
--  }

todosDigitosIguales :: Integer -> Bool

todosDigitosIguales n | n < 10 = True
                      | otherwise = ultimoDigito n == ultimoDigito (menosUltimo n) && todosDigitosIguales (menosUltimo n)

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

menosUltimo :: Integer -> Integer
menosUltimo n = div n 10

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
              | otherwise = 1 + cantDigitos(menosUltimo 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = ultimoDigito n
                 | otherwise = iesimoDigito (menosUltimo n) i