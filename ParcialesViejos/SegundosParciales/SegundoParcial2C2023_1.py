# Ejercicio 1
def acomodar(s:list[str]) -> list[str]:
    lista_up: list[str] = []
    lista_lla: list[str] = []
    for boleta in s:
        if boleta == "LLA":
            lista_lla.append(boleta)
        if boleta == "UP":
            lista_up.append(boleta)
    return lista_up + lista_lla
            

# Ejercicio 2
def pos_umbral(s: list[int], u: int) -> int:
    i: int = 0
    clientes_actuales: int = 0
    
    while (i < len(s)) and (clientes_actuales <= u):
        if s[i] > 0:
            clientes_actuales += s[i]
        i += 1
    
    if clientes_actuales <= u:
        return -1

    return (i - 1)

# Ejercicio 3
def es_columna_simetrica(s: list[int]) -> bool:
    primera_mitad: list[int] = []
    segunda_mitad: list[int] = []
    for i in range(int(len(s) / 2)):
        primera_mitad.append(s[i])
    for j in range(int(len(s) / 2), len(s)):
        segunda_mitad.append(s[j])
    return primera_mitad == segunda_mitad
        

def columnas_repetidas(mat: list[list[int]]) -> bool:
    for columna in mat:
        if not(es_columna_simetrica(columna)):
            return False
    return True
    
# Ejercicio 4
def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int,list[str]]) -> dict[str,list[int]]:
    res: dict[str, list[int]] = {}
    
    for nacion in naciones:
        res[nacion] = [0] * len(naciones)
    
    for yr in torneos.keys():
        length_yr_trnmt = len(torneos[yr])
        for i in range(length_yr_trnmt):
            res[torneos[yr][i]][i] += 1
    return res

if __name__ == "__main__":
    s = ["LLA", "UP", "LLA", "LLA", "UP"]
    print(acomodar(s))
    
    # ------------------------------------ #
    
    r = [1,-2,0,5,-7,3]
    u = 5
    print(pos_umbral(r,u))
    
    # ------------------------------------ #
    
    m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
    print(columnas_repetidas(m))
    
    # ------------------------------------ #
    
    naciones = ["arg", "aus", "nz", "sud"]
    torneos = {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
    print(cuenta_posiciones_por_nacion(naciones, torneos))
