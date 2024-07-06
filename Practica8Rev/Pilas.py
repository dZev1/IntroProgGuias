from queue import LifoQueue as Pila
from random import randint

# ej 1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p: Pila = Pila()
    for i in range(cantidad):
        n: int = randint(desde, hasta)
        p.put(n)
    return p

# ej 2
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

# ej 3
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

# ej 4
def buscar_nota_maxima(p: Pila[tuple[str,int]]) -> tuple[str, int]:
    elem: tuple[str,int] = p.get()
    pila_aux: Pila = Pila()
    max_actual = elem[1]
    pila_aux.put(elem)
    while not(p.empty()):
        elem = p.get()
        if elem[1] > max_actual:
            max_actual = elem[1]
        pila_aux.put(elem)
    while not(pila_aux.empty()):
        elem = pila_aux.get()
        p.put(elem)
    return max_actual

# ej 6
def evaluar_expresion(s: str) -> float:
    operadores: list[str] = ["+", "-", "*", "/"]
    pila_operandos: Pila[int] = Pila()
    op1: float
    op2: float
    resultado: float
    for i in s:
        if (i not in operadores) and (i != " "):
            pila_operandos.put(int(i))
        if i in operadores:
            op2 = pila_operandos.get()
            op1 = pila_operandos.get()
            if i == "+":
                resultado = op1 + op2
            if i == "-":
                resultado = op1 - op2
            if i == "*":
                resultado = op1 * op2
            if i == "/":
                resultado = op1 / op2
            pila_operandos.put(resultado)
    return resultado

# ej 7
def intercalar(p1: Pila, p2: Pila) -> Pila:
    pila_aux1: Pila = Pila()
    pila_aux2: Pila = Pila()
    res: Pila = Pila()
    res_aux: Pila = Pila()
    while not(p1.empty()) and not(p2.empty()):
        elem = p2.get()
        res_aux.put(elem)
        pila_aux2.put(elem)
        elem = p1.get()
        res_aux.put(elem)
        pila_aux1.put(elem)
    while not(pila_aux1.empty()):
        elem = pila_aux1.get()
        p1.put(elem)
    while not(pila_aux2.empty()):
        elem = pila_aux2.get()
        p2.put(elem)
    while not(res_aux.empty()):
        elem = res_aux.get()
        res.put(elem)
    return res

if __name__ == "__main__":
    pass
    
    
    
    