# AUXILIARES
def ordenados(arr: list[int]) -> list[int]:
    res: list[int] = arr.copy()
    longitud: int = len(arr)
    for i in range(longitud):
        intercambiado = False
        for j in range(0, longitud - i - 1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
                intercambiado = True
        if not intercambiado:
            return res
        
def cantidad_apariciones(e: str, s: str) -> int:
    contador: int = 0
    for elem in s:
        if e == elem:
            contador += 1
    return contador

# ej 5.1
def pertenece_a_cada_uno_v1(s: list[list[int]], e: int, res: list[bool]):
    res.clear()
    for linea in s:
        res.append(e in linea)

# v2 es igual a v1 en mi caso

# ej 5.3
def pertenece_a_cada_uno_v3(s: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []
    for linea in s:
        res.append(e in linea)
    return res

# ej 6.1
def es_matriz(m: list[list[int]]) -> bool:
    longitud_linea = len(m[0])
    for linea in m:
        if len(linea) != longitud_linea:
            return False
    return True

# ej 6.2
def filas_ordenadas(m: list[list[int]], res: list[bool]):
    res.clear()
    for linea in m:
        res.append(linea == ordenados(linea))

# ej 6.3
def columna(m: list[list[int]], c: int) -> list[int]:
    col: list[int] = []
    for linea in m:
        col.append(linea[c])
    return col

# ej 6.4
def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    col_actual: list[int] = []
    res: list[bool] = []
    for i in range(len(m[0])):
        col_actual = columna(m, i)
        res.append(col_actual == ordenados(col_actual))
    return res
        
# ej 6.5
def transponer(m: list[list[int]]) -> list[list[int]]:
    col_actual: list[int] = []
    res: list[list[int]] = []
    linea: list[int] = m[0]
    for i in range(len(linea)):
        col_actual = columna(m, i)
        res.append(col_actual)
    return res

# ej 6.6
def quien_gana_tateti(m: list[str]) -> int:
    col_actual: list[str] = []
    if m[0][0] == "X" and m[1][1] == m[0][0] and m[2][2] == m[0][0]:
        return 1
    if m[0][0] == "O" and m[1][1] == m[0][0] and m[2][2] == m[0][0]:
        return 0
    for i in range(len(m)):
        col_actual = columna(m, i)
        if cantidad_apariciones("X", col_actual) == 3 or cantidad_apariciones("X", m[i]) == 3:
            return 1
        if cantidad_apariciones("O", col_actual) == 3 or cantidad_apariciones("O", m[i]) == 3:
            return 0
    return 2