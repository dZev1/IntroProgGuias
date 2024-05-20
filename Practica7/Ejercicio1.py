def pertenece(s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if e == s[i]:
            return True
    return False

def divide_a_todos(s:list[int], e:int) -> bool:
    indice_actual:int = 0
    longitud_lista = len(s)

    while (indice_actual < longitud_lista):
        if s[indice_actual] % e != 0:
            return False
        else:
            indice_actual += 1
    return True

def suma_total(s: list[int]) -> int:
    suma: int = 0
    longitud_lista = len(s)
    for i in range(longitud_lista):
        suma += s[i]
    return suma
    
if __name__ == '__main__':
    print(pertenece([3,4,3,3,1,2,3,2,1,2,5,6,68,768,34,24,7], 68))
    print(suma_total([1,2,3]))
    print(divide_a_todos([2,4,6,8,2], 2))