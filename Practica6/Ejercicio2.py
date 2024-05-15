from math import sqrt 


def imprimir_saludo(nombre:str) -> None:
    print ("HOLA,", nombre)

def raiz_cuadrada_de_numero(numero:int) -> float:
    return sqrt(numero)

def fahrenheit_a_celsius(temp_far:float) -> float:
    return ((temp_far - 32) * 5) / 9

def imprimir_dos_veces_estribillo(estribillo:str) -> None:
    print(2 * estribillo)

def es_multiplo_de(n:int, m:int) -> bool:
    return n % m == 0

def es_par(n:int) -> bool:
    return es_multiplo_de(n, 2)

if __name__ == '__main__':
    imprimir_saludo("Diego")
    print(raiz_cuadrada_de_numero(10))
    print(fahrenheit_a_celsius(32))
    imprimir_dos_veces_estribillo("FATHAAAA\n")
    print(es_multiplo_de(6,4))
    print(es_par(4))

