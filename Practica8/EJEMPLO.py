def contar_elementos_pila(p: Pila[int]) -> int:
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

p = Pila()
p.put(23)
p.put(42)
p.put(3)
print(contar_elementos_pila(p))
print(contar_elementos_pila(p))