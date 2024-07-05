# 1.1
def pertenece(s: list[int], e: int) -> bool:
    for elem in s:
        if elem == e:
            return True
    return False

# 1.2
def divide_a_todos(s: list[int], e: int) -> bool:
    for elem in s:
        if elem % e != 0:
            return False
    return True

# 1.3
def suma_total(s: list[int]) -> int:
    suma_acum: int = 0
    for elem in s:
        suma_acum += elem
    return suma_acum

# 1.4
def maximo(s: list[int]) -> int:
    max_actual: int = s[0]
    for elem in s:
        if elem > max_actual:
            max_actual = elem
    return max_actual

# 1.5
def minimo(s: list[int]) -> int:
    min_actual: int = s[0]
    for elem in s:
        if elem < min_actual:
            min_actual = elem
    return min_actual

# 1.6
def ordenados(s: list[int]) -> list[int]:
    res: list[int] = []
    s_copy: list[int] = s.copy()
    for elem in s:
        min_s: int = minimo(s_copy)
        res.append(min_s)
        s_copy.remove(min_s)
    return res

# 1.7
def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    max_s: int = maximo(s)
    for i in range(len(s)):
        if s[i] == max_s:
            return i

# 1.8
def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    min_s: int = minimo(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == min_s:
            return i

# 1.9
def mayor_a_siete(lista_palabras: list[str]) -> bool:
    for palabra in lista_palabras:
        if len(palabra) > 7:
            return True
    return False

# 1.10
def reverso(s: str) -> str:
    res: str = ""
    for i in range(len(s) - 1, -1, -1):
        res += s[i]
    return res

def es_palindromo(palabra: str) -> bool:
    return palabra == reverso(palabra)

# 1.11
def tres_digitos_consecutivos_iguales(s: list[int]) -> bool:
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return True
    return False

# 1.12
def tres_vocales_distintas(palabra: str) -> bool:
    lista_vocales: list[str] = ["a", "e", "i", "o", "u"]
    vocales_aparecidas: list[str] = []
    for letra in palabra:
        if letra.lower() in lista_vocales and not letra.lower() in vocales_aparecidas:
            vocales_aparecidas.append(letra)
            if len(vocales_aparecidas) >= 3:
                return True
    return False

# 1.13
def posicion_secuencia_ordenada_mas_larga(lista):
    max_longitud: int = 0
    max_inicio: int = 0
    longitud_actual: int = 1
    inicio_actual: int = 0
    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:
            longitud_actual += 1
        else:
            if longitud_actual > max_longitud:
                max_longitud = longitud_actual
                max_inicio = inicio_actual
            longitud_actual = 1
            inicio_actual = i
    if longitud_actual > max_longitud:
        max_longitud = longitud_actual
        max_inicio = inicio_actual
    return max_inicio

# 1.14
def contar_impares(n: int) -> int:
    contador: int = 0
    n_str = str(n)
    for digito in n_str:
        if int(digito) % 2 != 0:
            contador +=1
    return contador

def cantidad_digitos_impares(s: list[int]) -> int:
    res: int = 0
    digitos_impares: int
    for numero in s:
        digitos_impares = contar_impares(numero)
        res += digitos_impares
    return res
