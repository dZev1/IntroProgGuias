from typing import IO

def contar_lineas(nombre_archivo: str) -> int:
    file: IO = open(nombre_archivo, "r")
    lineas: list[str] = file.readlines()

    file.close()

    return len(lineas)

def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    file: IO = open(nombre_archivo, "r")
    lineas: list[str] = file.readlines()
 
    file.close()
    
    for linea in lineas:
        if palabra in linea:
            return True
    return False

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
            

mi_archivo: str = "E:\Repos\IntroProgGuias\Practica8\ARTIMONKI.txt"

if __name__ == "__main__":
    print(contar_lineas(mi_archivo))
    print(existe_palabra("TOUT", mi_archivo))
    print(cantidad_apariciones(mi_archivo, "TOUT"))