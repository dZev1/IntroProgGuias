from typing import IO

# ej 21.1
def contar_lineas(nombre_archivo: str) -> int:
    file: IO = open(nombre_archivo, "r")
    lineas: list[str] = file.readlines()
    file.close()
    return len(lineas)

# ej 21.2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    file: IO = open(nombre_archivo, "r")
    lineas: list[str] = file.readlines()
    file.close()
    for linea in lineas:
        if palabra in linea:
            return True
    return False

# ej 21.3
def cantidad_apariciones(nombre_archivo: str, palabra:str) -> int:
    file: IO = open(nombre_archivo, "r")
    lineas: str = file.read()
    contador: int = 0
    palabras_en_lineas: list[str] = lineas.split()
    file.close()
    for palabras in palabras_en_lineas:
        if palabra in palabras:
            contador += 1
    return contador

# ej 22
def clonar_sin_comentarios(nombre_archivo: str) -> None:
    file: IO = open(nombre_archivo, "r")
    file_lines: list[str] = file.readlines()
    file_duplicate: IO = open(nombre_archivo + "_duplicado.txt", "w")
    file.close()
    for line in file_lines:
        if not(is_comment(line)):
            file_duplicate.write(line)
    file_duplicate.close()
    return None

def is_comment(line: str) -> bool:
    i: int = 0
    while (i < len(line) and line[i] == " "):
        i += 1
    return i < len(line) and line[i] == "#" 

# ej 23
def invertir_lineas(nombre_archivo: str):
    file: IO = open(nombre_archivo, "r")
    reverso: IO = open("reverso.txt", "w")
    lineas_file: list[str] = file.readlines()
    length = len(lineas_file)
    file.close()
    for i in range(length):
        reverso.write(lineas_file[length - 1 - i])
    reverso.close()

# ej 25
def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo: IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    archivo = open(nombre_archivo, "w")
    archivo.write(frase + "\n")
    for linea in lineas:
        archivo.write(linea)
