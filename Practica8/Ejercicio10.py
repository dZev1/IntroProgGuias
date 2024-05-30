from queue import LifoQueue as Pila
from random import randint

def parser_pila_lista(p: Pila[int]) -> list[int]:
    lista_de_pila: list[int] = []
    p_aux: Pila[int] = Pila()
    elem: int = 0
    while not(p.empty()):
        elem = p.get()
        p_aux.put(elem)
    while not(p_aux.empty()):
        elem = p_aux.get()
        lista_de_pila.append(elem)
        p.put(elem)
    return lista_de_pila

def buscar_el_maximo(p: Pila[int]) -> int:
    lista_pila: list[int] = parser_pila_lista(p)
    curr_max: int = lista_pila[0]

    for i in lista_pila:
        if i > curr_max:
            curr_max = i
    return curr_max

pila = Pila()
pila.put(randint(1,30))
pila.put(randint(1,30))
pila.put(randint(1,30))

if __name__ == "__main__":
    print(pila.queue)
    print(buscar_el_maximo(pila))

