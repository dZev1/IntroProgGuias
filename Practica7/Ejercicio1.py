def pertenece(s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if e == s[i]:
            return True
    return False

def suma_total(s: list[int]) -> int:
    suma: int = 0
    longitud_lista = len(s)
    for i in range(longitud_lista):
        suma += s[i]
    return suma
    
if __name__ == '__main__':
    print(pertenece([3,4,3,3,1,2,3,2,1,2,5,6,68,768,34,24,7], 9))
    print(suma_total([1,2,3]))

    input()