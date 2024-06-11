from queue import Queue as Cola

# Ej 1
def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str,str]]) -> Cola[str]:
    cola_comun: Cola[str] = Cola()
    cola_vip: Cola[str] = Cola()
    res: Cola[str] = Cola()
    filaClientesAux: Cola[tuple[str, str]] = Cola()
    persona: tuple[str, str] = ("","") 
    
    while not(filaClientes.empty()):
        persona = filaClientes.get()
        
        if persona[1] == "comun":
            cola_comun.put(persona[0])
        
        if persona[1] == "vip":
            cola_vip.put(persona[0])
            
        filaClientesAux.put(persona)
    
    while not(filaClientesAux.empty()):
        persona = filaClientesAux.get()
        filaClientes.put(persona)
    
    while not(cola_vip.empty()):
        res.put(cola_vip.get())
        
    while not(cola_comun.empty()):
        res.put(cola_comun.get())
    
    return res

# Ej 2
def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}
    
    for persona in estrategias.keys():
        res[persona] = 0
    
    for jugador1 in res.keys():
        for jugador2 in res.keys():
            if jugador1 != jugador2:
                if estrategias[jugador1] == "me desvio siempre" and estrategias[jugador2] == estrategias[jugador1]:
                    res[jugador1] -= 10
                if estrategias[jugador1] == "me la banco y no me desvio" and estrategias[jugador2] == estrategias[jugador1]:
                    res[jugador1] -= 5
                if estrategias[jugador1] == "me desvio siempre" and estrategias[jugador2] != estrategias[jugador1]:
                    res[jugador1] -= 15
                if estrategias[jugador1] == "me la banco y no me desvio" and estrategias[jugador2] != estrategias[jugador1]:
                    res[jugador1] += 10
    return res

# Ej 3
def quien_gano_el_tateti_facilito(tablero: list[str]) -> int:
    gano_ana: bool = False
    gano_beto: bool = False
    empate: bool = True
    longitud_tablero = len(tablero)
    columna: list[str] = []
    contador_x: int = 0
    contador_o: int = 0
    
    for i in range(longitud_tablero):
        columna: list[str] = []
        
        for fila in tablero:
            columna.append(fila[i])
        
        for caracter in columna:
            if caracter == "X" and contador_x < 3:
                contador_x += 1
                contador_o = 0
                
            if contador_x == 3:
                gano_ana = True
                empate = False
                
            if caracter == "O" and contador_o < 3:
                contador_o += 1
                contador_x = 0
                
            if contador_o == 3:
                gano_beto = True
                empate = False
                
            if caracter == " ":
                contador_o = 0
                contador_x = 0
    
    if empate or (gano_ana and gano_beto):
        return 3
    if gano_ana:
        return 1
    if gano_beto:
        return 0
    
# Ej 4
def es_palindromo(string: str) -> bool:
    string_reverso: str = ""
    for i in range(len(string) - 1, -1, -1):
        string_reverso += string[i]
    return string == string_reverso

def quitar_primera_letra(string: str) -> str:
    res: str = ""
    for i in range(len(string)):
        if i != 0:
            res += string[i]
    return res

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    contador: int = 0
    sufijo_actual = quitar_primera_letra(texto)
    if es_palindromo(texto) and texto != "":
        contador += 1
    
    while sufijo_actual != "":
        if es_palindromo(sufijo_actual):
            contador += 1
        sufijo_actual = quitar_primera_letra(sufijo_actual)
    return contador
    
if __name__ == "__main__":
    chicken_game = {
                "diego":"me la banco y no me desvio",
                "melina":"me desvio siempre",
                "rodrigo":"me la banco y no me desvio",
                "kevin": "me desvio siempre",
                "agustina": "me la banco y no me desvio"
                    }
    tateti_facilito =["XOOXOX",
                      "XOXOX ",
                      "XO     ",
                      "      ",
                      "      ",
                      "      "]
    print(torneo_de_gallinas(chicken_game))
    print(quien_gano_el_tateti_facilito(tateti_facilito))
    print(cuantos_sufijos_son_palindromos("aaaaaaaaaa"))
