-- Especificar e implementar las siguientes funciones, incluyendo su signatura:

-- absoluto: calcula el valor absoluto de un n´umero entero
absoluto :: Integer -> Integer
absoluto n | n >= 0 = n
           | n < 0 = -n

-- maximoabsoluto: devuelve el maximo entre el valor absoluto de dos numeros enteros
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m | absoluto n >= absoluto m = absoluto n
                   | absoluto m >= absoluto n = absoluto m

-- maximo3: devuelve el maximo entre tres numeros enteros.
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = x
              | otherwise = z

-- algunoEs0: dados dos numeros racionales, decide si alguno de los dos es igual a 0
algunoEs0 :: Float -> Float -> Bool
-- Pattern Matching
algunoEs0 x 0 = True
algunoEs0 0 x = True
algunoEs0 x y = False

-- algunoEs0 x y = x == 0 || y == 0

-- ambosSon0: dados dos numeros racionales, decide si ambos son iguales a 0
ambosSon0 :: Float -> Float -> Bool
-- Pattern Matching
ambosSon0 0 0 = True
ambosSon0 x y = False

-- ambosSon0 x y = x == 0 && y == 0

-- mismoIntervalo: dados dos numeros reales, indica si estan relacionados considerando la relacion de equivalencia en R
-- cuyas clases de equivalencia son: (−∞, 3],(3, 7] y (7, ∞), o dicho de otra forma, si pertenecen al mismo intervalo.
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x <= 7 && x > 3 && y <= 7 && y > 3 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

-- sumaDistintos: que dados tres numeros enteros calcule la suma sin sumar repetidos (si los hubiera).
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y + z
                    | x == y && x /= z = z
                    | x == z && x /= y = y
                    | y == z && y /= x = x
                    | otherwise = 0

-- esMultiploDe: dados dos numeros naturales, decidir si el primero es multiplo del segundo
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe n m | mod n m == 0 = True
                 | mod m n /= 0 = False
                 | otherwise = False

-- digitoUnidades: dado un numero entero, extrae su dıgito de las unidades.
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod (abs n) 10

-- digitoDecenas: dado un numero entero, extrae su dıgito de las decenas.
digitoDecenas :: Integer -> Integer
digitoDecenas n = digitoUnidades (div (abs n) 10)
-- otra forma: digitoDecenas n = div (mod (abs n) 100 - mod (abs n) 10) 10
