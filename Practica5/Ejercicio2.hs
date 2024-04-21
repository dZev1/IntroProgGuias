-- Definir las siguientes funciones sobre listas:

-- pertenece :: (Eq t) => t -> [t] -> Bool según la siguiente especificacion:
-- problema pertenece (e: T , s: seq⟨T⟩) : B {
--  requiere: { True }
--  asegura: { resultado = true ↔ e ∈ s }
-- }
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece t (x:xs) | t == x = True
                   | otherwise = pertenece t xs

-- todosIguales :: (Eq t) => [t] -> Bool, que dada una lista devuelve verdadero si y solamente si
-- todos sus elementos son iguales.
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [t] = True
todosIguales (t:ts) = t == head ts && todosIguales ts

-- todosDistintos :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
-- problema todosDistintos (s: seq⟨T⟩) : B {
--  requiere: { True }
--  asegura: { resultado = False ↔ existen dos posiciones distintas de s con igual valor }
-- }
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [t] = True
todosDistintos (t:ts) = not (pertenece t ts) && todosDistintos ts

-- hayRepetidos :: (Eq t) => [t] -> Bool segun la siguiente especificacion:
-- problema hayRepetidos (s: seq⟨T⟩) : B {
--  requiere: { True }
--  asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
-- }
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (t:ts) | pertenece t ts = True
                    | otherwise = hayRepetidos ts
