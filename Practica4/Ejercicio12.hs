raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = 1 + 1 / raizDe2AproxAux (n - 1)

raizDe2AproxAux :: Integer -> Float
raizDe2AproxAux 1 = 2
raizDe2AproxAux n = 2 + 1 / raizDe2AproxAux (n - 1)