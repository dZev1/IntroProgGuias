-- Implementar una funcion parcial f:: Integer -> Integer definida por extensión de la siguiente manera:
-- f(1) = 8 ; f(4) = 131 ; f(16) = 16

f :: Integer -> Integer
g :: Integer -> Integer
h :: Integer -> Integer
k :: Integer -> Integer

f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

-- Análogamente definir e implementar g :: Integer -> Integer
-- g(8) = 16 ; g(16) = 4 ; g(131) = 1

g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

-- A partir de las funciones f Y g, implementar las funciones h = f o g y k = g o f

h n | n == 8 = f (g 8)
    | n == 16 = f (g 16)
    | n == 131 = f (g 131)

k n | n == 1 = g (f 1)
    | n == 4 = g (f 4)
    | n == 16 = g (f 16)
