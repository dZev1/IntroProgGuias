import Simulacro
import Test.HUnit

main = runTestTT tests

tests = test [
--"nombre" ~: (funcion parametros) ~?= resultado_esperado
    "componentes repetidas" ~: (relacionesValidas [("ana", "ana")]) ~?= False,
    "tupla repetida" ~: (relacionesValidas [("ana", "pedro"), ("ana", "pedro")]) ~?= False,
    "tupla repetida invertida" ~: (relacionesValidas [("ana", "pedro"), ("pedro", "ana")]) ~?= False,
    "todas diferentes" ~: (relacionesValidas [("ana", "pedro"), ("ana", "carlos")]) ~?= True
    ]
