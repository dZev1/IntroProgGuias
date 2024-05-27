# EJ 1
def pertenece(s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if e == s[i]:
            return True
    return False

# EJ 2
def divide_a_todos(s: list[int], e: int) -> bool:
    indice_actual:int = 0
    longitud_lista = len(s)

    while (indice_actual < longitud_lista):
        if s[indice_actual] % e != 0:
            return False
        else:
            indice_actual += 1
    return True

# EJ 3

def suma_total(s: list[int]) -> int:
    suma: int = 0
    longitud_lista = len(s)
    for i in range(longitud_lista):
        suma += s[i]
    return suma

# EJ 4
def ordenados (s: list[int]) -> list[int]:
    lista_desordenada: list[int] = s.copy()
    lista_ordenada: list[int] = []
    longitud: int = len(s)
    
    while longitud > 0:
        lista_ordenada.append(min(lista_desordenada))
        lista_desordenada.remove(min(lista_desordenada))
        longitud -= 1

    return lista_ordenada

# EJ 5            
def longitud_mayor_a_7(lista: list[str]) -> bool:
    longitud = len(lista)
    for i in range(longitud):
        if len(lista[i]) >= 7:
            return True
    return False

# EJ 6
def palindromo(a: str) -> bool:
    r: str = a
    r = r.lower()
    return r == r[::-1]

# EJ 7
def tiene_algun_numero(s: str) -> bool:
    longitud :int = len(s)
    for i in range(longitud):
        if (s[i] >= "0") and (s[i] <= "9"):
            return True
    return False

def tiene_mayus(s: str) -> bool:
    longitud: int = len(s)
    for i in range(longitud):
        if (s[i] >= "A") and (s[i] <= "Z"):
            return True
    return False

def tiene_minus(s: str) -> bool:
    longitud: int = len(s)
    for i in range(longitud):
        if (s[i] >= "a") and (s[i] <= "z"):
            return True
    return False

def fortaleza_password(s: str) -> str:
    password: str = s
    longitud_mayor_a_8: bool = len(password) > 8
    longitud_menor_a_5: bool = len(password) < 5
    tiene_numeros: bool = tiene_algun_numero(password)
    tiene_mayus_minus = tiene_mayus(password) and tiene_minus(password)
    
    if longitud_mayor_a_8 and tiene_numeros and tiene_mayus_minus:
        return "VERDE"
    elif longitud_menor_a_5:
        return "ROJO"
    else:
        return "AMARILLO"

# EJ 8
def historial_movimientos(t:list[tuple[str,int]]) -> int:
    saldo: int = 0
    length: int = len(t)
    
    for i in range(length):
        if t[i][0] == "I":
            saldo += t[i][1]
        if t[i][0] == "R":
            saldo -= t[i][1]

    return saldo


if __name__ == "__main__":
    print("ANA es palindromo?:", palindromo("ANa"))
    a = [("I", 30000),("R",4300),("I",200)]
    print(historial_movimientos(a))