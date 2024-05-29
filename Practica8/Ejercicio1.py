import typing

def contar_lineas(nombre_archivo: str) -> int:
    file: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = file.readlines()

    file.close()

    return len(lineas)



mi_archivo: str = "HolaMundo.txt"

if __name__ == "__main__":
    print(contar_lineas(mi_archivo))