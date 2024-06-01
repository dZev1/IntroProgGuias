from queue import LifoQueue as Pila
from random import randint

def buscar_el_maximo(p: Pila[int]) -> int:
    max_actual: int = p.get()
    pila_aux: Pila = Pila()
    elem: int
    
    pila_aux.put(max_actual)
    
    while not(p.empty()):
        elem = p.get()
        if elem > max_actual:
            max_actual = elem
        pila_aux.put(elem)
    
    while not(pila_aux.empty()):
        elem = pila_aux.get()
        p.put(elem)
    
    return max_actual

pila = Pila()
pila.put(randint(1,30))
pila.put(randint(1,30))
pila.put(randint(1,30))
pila.put(randint(1,30))
pila.put(randint(1,30))
pila.put(randint(1,30))

if __name__ == "__main__":
    print(pila.queue)
    print(buscar_el_maximo(pila))