sumaDoble :: Integer -> Integer -> Integer
sumaDoble 0 m = 0
sumaDoble n m = sumaInterior n m + sumaDoble (n - 1) m

sumaInterior :: Integer -> Integer -> Integer
sumaInterior n 0 = 0
sumaInterior n m = n ^ m + sumaInterior n (m - 1) 