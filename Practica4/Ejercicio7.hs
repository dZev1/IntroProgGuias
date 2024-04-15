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