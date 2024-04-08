--1.A
f :: Integer -> Integer

f 1 = 8
f 4 = 131
f 16 = 16

--1.B
g :: Integer -> Integer

g 8 = 16
g 16 = 4
g 131 = 1

--1.C
h :: Integer -> Integer
k :: Integer -> Integer

h n = f (g n)

k n = g (f n)