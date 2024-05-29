def reemplazar_pares(s:list[int]) -> list[int]:
    length: int = len(s)
    for i in range(length):
        if i % 2 == 0:
            s[i] = 0
            
def reemplazar_pares_in(s:list[int]) -> list[int]:
    length: int = len(s)
    result: list[int] = s.copy()
    for i in range(length):
        if i % 2 == 0:
            result[i] = 0
    return result
    
def quitar_vocales(s:str) -> str:
    vocales: list[str] = ['a','e','i','o','u','A','E','I','O','U']
    
    for i in s:
        if i in vocales:
            s = s.replace(i, "")
    return s
    
def reemplaza_vocales(s: str) -> str:
    vocales: list[str] = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if i in vocales:
            s = s.replace(i, "_")
    return s

def da_vuelta_str(s: str) -> str:
    result: str = ""
    for i in range(1, len(s) + 1):
        result += s[len(s) - i]
    return result

def eliminar_repetidos(s:str) -> str:
    res: str = ""
    for i in s:
        if not i in res:
            res += i
    return res


a = [1,34,2,19,340,20,13,42,10]
b = "Hola como estas"

if __name__ == "__main__":
    s = "hola"
    
    print(quitar_vocales(s))
    print(reemplaza_vocales(s))
    print(da_vuelta_str(s))
    print(eliminar_repetidos(b))