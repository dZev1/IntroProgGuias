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
    


a = [1,34,2,19,340,20,13,42,10]
b = "Hola como estas"

if __name__ == "__main__":
    s = "hola"
    
    print(quitar_vocales(s))