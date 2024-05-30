from typing import IO

def invertir_lineas(nombre_archivo: str):
    file: IO = open(nombre_archivo, "r")
    reverso: IO = open("reverso.txt", "w")
    lineas_file: list[str] = file.readlines()
    length = len(lineas_file)
    
    
    file.close()
    
    for i in range(length):
        reverso.write(lineas_file[length - 1 - i])
    reverso.close()
        
if __name__ == "__main__":
    invertir_lineas("E:\Repos\IntroProgGuias\Practica8\ARTIMONKI.txt")