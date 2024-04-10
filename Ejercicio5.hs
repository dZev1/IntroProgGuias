-- Implementar la funcion todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores :: (Int,Int,Int) -> Bool
f :: Int -> Int
g :: Int -> Int

todosMenores (n1,n2,n3) = f n1 > g n1 && f n2 > g n2 && f n3 > g n3

f n | n <= 7 = n * n
    | n > 7 = 2 * n - 1

g n | even n = div n 2
    | otherwise = 3 * n + 1