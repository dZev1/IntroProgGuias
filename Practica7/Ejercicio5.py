def pertenece(s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if e == s[i]:
            return True
    return False

def pertenece_a_cada_uno_version_2(s:list[list[int]], e: int, result:list[bool]):
    result.clear()
    length: int = len(s)
    for i in range(length):
        result.append(pertenece(s[i],e))
    return result 

def es_matriz(s:list[list[int]]) -> bool:
    length: int = len(s)
    length_first_elem: int = len(s[0])
    for i in range(length):
        if not (len(s[i]) == len(s[0])):
            return False
    return True

def filas_ordenadas(m:list[list[int]], res: list[bool]):
    res.clear()
    length: int = len(m)
    for i in range(length):
        res.append(ordenados(m[i]))
    return res
    
def ordenados (s: list[int]) -> list[int]:
    lista_desordenada: list[int] = s.copy()
    lista_ordenada: list[int] = []
    longitud: int = len(s)
    
    while longitud > 0:
        lista_ordenada.append(min(lista_desordenada))
        lista_desordenada.remove(min(lista_desordenada))
        longitud -= 1

    return lista_ordenada

a: list[list[int]] = [[3,4,5], [2,8,4], [322343,43,54]]


if __name__ == '__main__':
    print(pertenece_a_cada_uno_version_2(a, 4, []))
    print(es_matriz(a))
    print(filas_ordenadas(a,[[132,34,32],[232,3,2],[2,3,4]]))
    print(a)
