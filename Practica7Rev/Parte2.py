# ej 2.1
def eliminar_pares_inout(s: list[int]):
    for i in range(len(s)):
        if s[i] % 2 == 0:
            s[i] = 0

# ej 2.2
def eliminar_pares_in(s: list[int]) -> list[int]:
    res: list[int] = []
    for elem in s:
        if elem % 2 == 0:
            res.append(0)
        else:
            res.append(elem)
    return res

# ej 2.3
def eliminar_vocales(palabra: str) -> str:
    res: str = ""
    lista_vocales: list[str] = ["a", "e", "i", "o", "u"]
    for letra in palabra:
        if letra.lower() not in lista_vocales:
            res += letra
    return res

# ej 2.4
def reemplaza_vocales(s: str) -> str:
    res: str = ""
    lista_vocales: list[str] = ["a", "e", "i", "o", "u"]
    for letra in s:
        if letra.lower() in lista_vocales:
            res += "_"
        else:
            res += letra
    return res

# ej 2.5
def da_vuelta_str(s:str) -> str:
    res: str = ""
    for i in range(len(s) - 1, -1, -1):
        res += s[i]
    return res

# ej 2.6
def cantidad_apariciones(e: str, s: str) -> int:
    contador: int = 0
    for elem in s:
        if e == elem:
            contador += 1
    return contador

def eliminar_repetidos(s: str) -> str:
    res = ""
    for letra in s:
        if cantidad_apariciones(letra, s) == 1:
            res += letra
    return res

# ej 3
def aprobado(notas: list[int]) -> int:
    length: int = len(notas)
    suma_de_notas: int = 0
    promedio: int = 0
    contador: int = 0
    resultado: int = 0
    for nota in notas:
        if nota >= 4:
            suma_de_notas += nota
            contador += 1
        if nota < 4:
            resultado = 3
            return resultado
    promedio = suma_de_notas / length
    if promedio >= 7 and contador == length:
        resultado = 1
    else:
        resultado = 2
    return resultado

# ej 4
def historial_movimientos(t:list[tuple[str,int]]) -> int:
    saldo: int = 0
    length: int = len(t)
    for i in range(length):
        if t[i][0] == "I":
            saldo += t[i][1]
        if t[i][0] == "R":
            saldo -= t[i][1]
    return saldo