def reemplazar_pares(s:list[int]) -> list[int]:
    length: int = len(s)
    for i in range(length):
        if i % 2 == 0:
            s[i] = 0
    return s

def reemplazar_pares_in(s:list[int]) -> list[int]:
    length: int = len(s)
    result: list[int] = s.copy()
    for i in range(length):
        if i % 2 == 0:
            result[i] = 0
    return result
    

a = [1,34,2,19,340,20,13,42,10]
b = "Hola como estas"

if __name__ == "__main__":
    pass
    