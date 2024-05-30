from queue import LifoQueue as Pila

def cantidad_elementos(p: Pila[int]) -> int:
    cantidad: int = 0
    pila_aux = Pila()
    while not(p.empty()):
        elem = p.get()
        cantidad += 1
        pila_aux.put(elem)
    
    while not(pila_aux.empty()):
        elem = pila_aux.get()
        p.put(elem)
    return cantidad