-- Programar una funcion bisiesto :: Integer ->Bool 
bisiesto :: Int -> Bool
bisiesto yr | mod yr 4 == 0 && (mod yr 100 /= 0 || mod yr 400 == 0) = True
            | otherwise = False