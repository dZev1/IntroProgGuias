from queue import LifoQueue as Pila
from random import randint

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p: Pila = Pila()
    for i in range(cantidad):
        n: int = randint(desde, hasta)
        p.put(n)
    return p

pila = generar_nros_al_azar(12,3,1230)
print(pila.queue)