def lista_de_estudiantes() -> list[str]:
    palabra_ingresada: str = ""
    palabra_ingresada = input("Ingrese un nombre: ")
    lista_estudiantes: list[str] = []
    
    while palabra_ingresada != "listo":
        lista_estudiantes.append(palabra_ingresada)
        palabra_ingresada = input("Ingrese un nombre: ")
    
    return lista_estudiantes

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
            
if __name__ == "__main__":
    print(lista_de_estudiantes())
    print(historial_movimientos())
    
