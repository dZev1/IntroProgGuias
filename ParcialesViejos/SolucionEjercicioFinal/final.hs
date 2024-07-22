esSudokuValido :: [[Int]] -> Bool
esSudokuValido xs = todasFilasValidas xs && todasFilasValidas (transponer xs)

transponer :: [[Int]] -> [[Int]]
transponer xs 
    | not (tieneColumnas xs) = []
    | otherwise = primeraColumna xs : transponer (borrarPrimeraColumna xs)

borrarPrimeraColumna :: [[Int]] -> [[Int]]
borrarPrimeraColumna [] = []
borrarPrimeraColumna ([]:_) = []
borrarPrimeraColumna ((y:ys):xs) = ys : borrarPrimeraColumna xs

tieneColumnas :: [[Int]] -> Bool
tieneColumnas [] = False
tieneColumnas ([]:xs) = tieneColumnas xs
tieneColumnas _ = True

primeraColumna :: [[Int]] -> [Int]
primeraColumna [] = []
primeraColumna ([]:_) = []
primeraColumna ((y:ys):xs) = y : primeraColumna xs

todasFilasValidas :: [[Int]] -> Bool
todasFilasValidas [] = True
todasFilasValidas (x:xs) = esFilaValida 9 x && todasFilasValidas xs

esFilaValida :: Int -> [Int] -> Bool
esFilaValida _ [] = True
esFilaValida 0 _ = True
esFilaValida n xs
    | cantidadApariciones n xs > 1 = False
    | otherwise = esFilaValida (n - 1) xs

cantidadApariciones :: Int -> [Int] -> Int
cantidadApariciones _ [] = 0
cantidadApariciones n (x:xs)
    | n == x = 1 + cantidadApariciones n xs
    | otherwise = cantidadApariciones n xs

-- CASO 1: # [[1,2,3,4,5,6,7,8,9],[9,3,7,6,4,5,3,2,1],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,4,0,0,0],[0,0,0,0,6,0,0,0,0],[0,0,0,5,0,0,0,0,0],[0,0,4,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,0]]
-- OUTPUT: FALSE
-- CASO 2: # [[1,2,3,4,5,6,7,8,9],[9,8,7,6,4,5,3,2,1],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,4,0,0,0],[0,0,0,0,6,0,0,0,0],[0,0,0,5,0,0,0,0,0],[0,0,4,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,0]]
-- OUTPUT: TRUE
