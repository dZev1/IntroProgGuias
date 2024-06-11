from typing import IO
from queue import LifoQueue as Pila
def maximo(l: list[int]) -> int:
    curr_max: int = l[0]
    length: int = len(l)
    for i in range(length):
        if l[i] > curr_max:
            curr_max = l[i]
    return curr_max
    
# 19
def agrupar_por_longitud(nombre_archivo: str) -> dict[int, int]:
    res: dict[int, int] = {}
    file = open(nombre_archivo, "r")
    palabras_archivo: list[str] = file.read().split()
    file.close()
    for palabra in palabras_archivo:
        if len(palabra) not in res.keys():
            res[len(palabra)] = 1
        else:
            res[len(palabra)] += 1
    return res

# 21
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    res: dict[str, int] = {}
    file: IO = open(nombre_archivo, "r")
    palabras_archivo: list[str] = file.read().split()
    file.close
    lista: list[int] = []
    
    for palabra in palabras_archivo:
        if palabra not in res.keys():
            res[palabra] = 1
        else:
            res[palabra] += 1
    
    for value in res.values():
        lista.append(value)

    max_lista: int = maximo(lista)
    
    for clave in res:
        if max_lista == res[clave]:
            return clave
    
# 22
def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str):
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)
    
def navegar_atras(historiales: dict[str, Pila[str]], usuario: str):
    elem = historiales[usuario].get()
    sitio_anterior = historiales[usuario].get()
    historiales[usuario].put(sitio_anterior)
    historiales[usuario].put(elem)
    historiales[usuario].put(sitio_anterior)


p = Pila()
p.put("google.com")
p.put("youtube.com")
p.put("web.whatsapp.com")

archivo: str = "ARTIMONKI.txt"
historiales: dict[str, Pila[str]] = {"dz1" : p}

if __name__ == "__main__":
    print(la_palabra_mas_frecuente(archivo))
    
    visitar_sitio(historiales, "dz1", "twitch.tv")
    print(historiales["dz1"].queue)
    navegar_atras(historiales, "dz1")
    print(historiales["dz1"].queue)