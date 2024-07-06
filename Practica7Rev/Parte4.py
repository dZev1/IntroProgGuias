# ej 7.1
def lista_estudiantes() -> list[str]:
    palabra_ingresada: str = ""
    palabra_ingresada = input("Ingrese un nombre: ")
    lista_estudiantes: list[str] = []
    while palabra_ingresada not in ["listo", ""]:
        lista_estudiantes.append(palabra_ingresada)
        palabra_ingresada = input("Ingrese un nombre: ")
    return lista_estudiantes
        
# ej 7.2
def historial_movimientos() -> list[tuple[str, int]]:
    usuario_desea: str = ""
    monto: int = 0
    resultado: list[tuple[str,int]] = []
    usuario_desea = input("Que desea realizar? ('C' para cargar, 'D' para descontar o 'X' para salir): ")
    while usuario_desea != "X":
        if usuario_desea == 'C':
            monto = int(input("Cuanto desea cargar: "))
            resultado.append((usuario_desea, monto))
        if usuario_desea == 'D':
            monto = int(input("Cuanto desea descontar: "))
            resultado.append((usuario_desea, monto))
        usuario_desea = input("Que desea realizar? ('C' para cargar, 'D' para descontar o 'X' para salir): ")
    return resultado

# ej 7.4
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

def fortaleza_password() -> str:
    password: str = input("Introduzca una contraseña: ")
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