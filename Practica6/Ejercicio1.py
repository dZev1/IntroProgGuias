from math import sqrt
from math import pi

def imprimir_hola_mundo() -> str:
    return "Hello World!"

def imprimir_un_verso() -> str:
    return "And if a double-decker bus,\nCrashes into us.\nTo die by your side,\nIs such a heavenly way to die."

def raizDe2() -> float:
    return round(sqrt(2),4)

def factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_de_dos() -> int:
    return factorial(2)

def perimetro() -> float:
    return 2 * pi

if __name__ == "__main__":
    print(imprimir_hola_mundo())
    print(imprimir_un_verso())
    print(raizDe2())
    print(factorial_de_dos())
    print(perimetro())