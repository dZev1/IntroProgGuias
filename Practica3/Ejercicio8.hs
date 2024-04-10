comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos b < sumaUltimosDosDigitos a = -1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0

digitoUnidades :: Integer -> Integer
digitoUnidades n = mod (abs n) 10

digitoDecenas :: Integer -> Integer
digitoDecenas n = digitoUnidades (div (abs n) 10)

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = digitoUnidades x + digitoDecenas x