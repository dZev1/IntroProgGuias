from queue import Queue as Cola
import random

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c = Cola()

    for i in range(cantidad):
        elem = random.randint(desde, hasta)
        c.put(elem)
    return c

def cantidad_elementos(c: Cola) -> int:
    longitud: int = 0
    c_aux: Cola = Cola()
    
    while not(c.empty()):
        elem = c.get()
        longitud += 1
        c_aux.put(elem)

    while not(c_aux.empty()):
        elem = c_aux.get()
        c.put(elem)
    
    return longitud

# 15
def buscar_el_maximo(c: Cola[int]) -> int:
    c_aux: Cola[int] = Cola()
    elem: int = c.get()
    current_max: int = elem
    c_aux.put(elem)
    
    while not(c.empty()):
        elem = c.get()
        if elem > current_max:
            current_max = elem
        c_aux.put(elem)

    while not(c_aux.empty()):
        elem = c_aux.get()
        c.put(elem)
        
    return current_max


# 16
# A
def pertenece(e: int, s: list[int]) -> bool:
    for elem in s:
        if e == elem:
            return True
    return False

def armar_secuencia_de_bingo() -> Cola[int]:
    sec_bingo: Cola[int] = Cola()
    numeros_0_99: list[int] = list(range(0,99))
    random.shuffle(numeros_0_99)
    
    for i in range(99):
        sec_bingo.put(numeros_0_99[i])

    return sec_bingo

#B
def jugar_carton_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    cantidad_jugadas: int = 1
    coincidencias: int = 0
    longitud_carton: int = len(carton)
    bolilla: int
    cola_aux = Cola()

    while coincidencias < longitud_carton:
        bolilla: int = bolillero.get()
        if pertenece(bolilla, carton):
            coincidencias += 1
        cantidad_jugadas += 1
        cola_aux.put(bolilla)

    while not(cola_aux.empty()):
        bolilla = cola_aux.get()
        bolillero.put(bolilla)

    return cantidad_jugadas

