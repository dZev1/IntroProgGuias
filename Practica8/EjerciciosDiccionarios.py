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