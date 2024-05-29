from typing import IO

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


if __name__ == "__main__":
    clonar_sin_comentarios("/home/Estudiante/Escritorio/IntroProgGuias/Practica8/ARTIMONKI.txt")
