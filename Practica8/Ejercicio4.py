from typing import IO
def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo: IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    
    archivo = open(nombre_archivo, "w")
    archivo.write(frase + "\n")
    
    for linea in lineas:
        archivo.write(linea)


if __name__ == "__main__":
    agregar_frase_al_principio("JELOUEVERYBODY.txt", "RAND AL'THOR, EL DRAGON")