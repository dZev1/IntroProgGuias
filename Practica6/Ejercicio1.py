from math import sqrt, pi

def print_hello_world() -> None:
    print("Hello, World!")

def imprimir_un_verso() -> None:
    print("We are the Edema Ruh.\nWe know the songs,\nThat sirens sang")

def raiz_de_2() -> str:
    return round(sqrt(2),4)

def factorial_de_2() -> int:
    return 2 * 1

def perimetro() -> float:
    return 2 * pi



if __name__ == '__main__':
    print_hello_world()
    imprimir_un_verso()
    print(raiz_de_2())
    print(factorial_de_2())
    print(perimetro())