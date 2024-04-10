-- Especificar e implementar las siguientes funciones utilizando tuplas para representar pares, ternas de numeros.

-- prodInt: calcula el producto interno entre dos tuplas R × R
prodInt :: (Float,Float) -> (Float, Float) -> Float
prodInt (v1,v2) (w1,w2) = v1 * w1 + v2 * w2

-- todoMenor: dadas dos tuplas R×R, decide si es cierto que cada coordenada de la primera tupla es menor a la coordenada correspondiente de la segunda tupla.
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (t11, t12) (t21, t22) = t11 < t21 && t12 < t22

-- distanciaPuntos: calcula la distancia entre dos puntos de R2
distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (v1,v2) (w1,w2) = sqrt((v1 - w1)^2 + (v2-w2)^2)

-- sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.
sumaTerna :: (Int,Int,Int) -> Int
sumaTerna (x1,x2,x3) = x1 + x2 + x3

-- sumarSoloMultiplos: dada una terna de numeros enteros y un natural, calcula la suma de los elementos de la terna que son multiplos del numero natural.
-- Ej: (10,-8,-5) 2 = 2 = (10 + (-8))
sumarSoloMultiplos :: (Int,Int,Int) -> Int -> Int
sumarSoloMultiplos (n1,n2,n3) m | mod (abs n1) (abs m) == 0 && mod (abs n2) (abs m) == 0 && mod (abs n3) (abs m) == 0 = n1 + n2 + n3
                                | mod (abs n1) (abs m) == 0 && mod (abs n2) (abs m) /= 0 && mod (abs n3) (abs m) /= 0 = n1
                                | mod (abs n1) (abs m) /= 0 && mod (abs n2) (abs m) == 0 && mod (abs n3) (abs m) /= 0 = n2
                                | mod (abs n1) (abs m) /= 0 && mod (abs n2) (abs m) /= 0 && mod (abs n3) (abs m) == 0 = n3
                                | mod (abs n1) (abs m) == 0 && mod (abs n2) (abs m) == 0 && mod (abs n3) (abs m) /= 0 = n1 + n2
                                | mod (abs n1) (abs m) == 0 && mod (abs n2) (abs m) /= 0 && mod (abs n3) (abs m) == 0 = n1 + n3
                                | mod (abs n1) (abs m) /= 0 && mod (abs n2) (abs m) == 0 && mod (abs n3) (abs m) == 0 = n2 + n3
                                | otherwise = 0

-- posPrimerPar: dada una terna de enteros, devuelve la posicion del primer numero par si es que hay alguno, y devuelve 4 si son todos impares.
posPrimerPar :: (Int,Int,Int) -> Int
posPrimerPar (n1,n2,n3) | even n1 = 0
                        | even n2 = 1
                        | even n3 = 2
                        | otherwise = 4

-- crearPar :: a ->b ->(a, b): crea un par a partir de sus dos componentes dadas por separado (debe funcionar para elementos de cualquier tipo).
crearPar :: a -> b -> (a, b)
crearPar a b = (a,b)

-- invertir :: (a, b) ->(b, a): invierte los elementos del par pasado como par´ametro (debe funcionar para elementos de cualquier tipo).
invertir :: (a,b) -> (b, a)
invertir (x,y) = (y,x)