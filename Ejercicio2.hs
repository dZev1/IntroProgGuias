--2. C
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = x
              | otherwise = z

--2. G
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y + z
                    | x == y && x /= z = z
                    | x == z && x /= y = y
                    | y == z && y /= x = x
                    | otherwise = 0

--2. I

digitoUnidades :: Integer -> Integer

digitoUnidades n = mod (abs n) 10

digitoDecenas :: Integer -> Integer

-- 1era forma: digitoDecenas n = div (mod (abs n) 100 - mod (abs n) 10) 10
-- 2da forma:
digitoDecenas n = digitoUnidades (div (abs n) 10)
