# Auxiliares
def maximo(lista: list[int]) -> int:
    curr_max = lista[0]
    for i in lista:
        if i > curr_max:
            curr_max = i
    return curr_max

def minimo(lista: list[int]) -> int:
    curr_min = lista[0]
    for i in lista:
        if i < curr_min:
            curr_min = i
    return curr_min

def es_primo(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Ej 1
def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res: list[int] = []
    for codigo in codigos_barra:
        if es_primo(codigo % 1000):
            res.append(codigo)
    return res

# Ej 2
def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    res: dict[str, tuple[int, int]] = {}
    lista_stock: list[int] = []
    maximum: int = 0
    minimum: int = 0
    for tupla in stock_cambios:
        if not(tupla[0] in res.keys()):
            res[tupla[0]] = (0, 0)
    for key in res:
        lista_stock = []
        for elem in stock_cambios:
            if key == elem[0]:
                lista_stock.append(elem[1])
        maximum = maximo(lista_stock)
        minimum = minimo(lista_stock)
        res[key] = (minimum, maximum)
    return res
                 
# Ej 3
def cant_apariciones(palabra: str, lista: list[str]) -> int:
    res: int = 0
    for i in lista:
        if palabra == i:
            res += 1
    return res

def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool,bool]]:
    grilla_horaria_morning: list[list[str]] = []
    grilla_horaria_afternoon: list[list[str]] = []
    lista_res: list[tuple[bool, bool]] = []
    tupla_bool: tuple[bool, bool] = (False, False)
    
    # hago dos listas, cada una siendo una mitad de la tabla.
    # la primera es la mañana, la segunda la tarde
    for i in range(int(len(grilla_horaria) / 2)):
        grilla_horaria_morning.append(grilla_horaria[i])
    for i in range(int(len(grilla_horaria) / 2), len(grilla_horaria)):
        grilla_horaria_afternoon.append(grilla_horaria[i])
    
    for j in range(len(grilla_horaria_morning[0])):
        # veo si cada columna de la mañana tiene sus cuatro componentes iguales
        columna: list[str] = []
        
        for linea in grilla_horaria_morning:
            columna.append(linea[j])
        horarios_manana = cant_apariciones(columna[0], columna) == 4
            
        # veo si cada columna de la tarde tiene sus cuatro componentes iguales
        columna: list[str] = []
        for linea in grilla_horaria_afternoon:
            columna.append(linea[j])
        horarios_tarde = cant_apariciones(columna[0], columna) == 4
        
        tupla_bool = (horarios_manana, horarios_tarde)
        lista_res.append(tupla_bool)
    
    # armo la lista res con cada uno de los valores obtenidos de las iteraciones anteriores
    return lista_res

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    historial_cadena: list[tuple[int, int]] = []
    paciente_n: int = 0
    
    while paciente_n < len(tipos_pacientes_atendidos):
        inicio_cadena: int = paciente_n
        cadena: int = 0
        while paciente_n < len(tipos_pacientes_atendidos) and tipos_pacientes_atendidos[paciente_n] == tipos_pacientes_atendidos[inicio_cadena]:
            cadena += 1
            paciente_n += 1
            historial_cadena.append((inicio_cadena, cadena))
        paciente_n += 1
        
    cadena_max: int = 0
    
    for (inicio_cadena, cadena) in historial_cadena:
        if cadena > cadena_max:
            cadena_max = cadena
            inicio_cadena_max: int = inicio_cadena
    return inicio_cadena_max

if __name__ == "__main__":
    lista_codigos = [123373041,123373010,123373037,123373027,123373090,1233730107]
    print(filtrar_codigos_primos(lista_codigos))
    
    a_stock = [("penis",12),("gargola",23),("penis",0),("calculadora casio fx-94", 3478), ("gargola",10),("gargola",5),("calculadora casio fx-94", 5000)]
    print(stock_productos(a_stock))
    
    matriz_horaria = [
                    ["claudia","fernando","winston","lucio","omen","ruckus","viktor"],
                    ["claudia","roberto","winston","lucio","ruckus","ruckus","viktor"],
                    ["claudia","fernando","jeronimo","lucio","omen","ruckus","d.va"],
                    ["claudia","micho","tito","gordo","cabezon","ruckus","viktor"],
                    ["claudia","fernando","winston","lucio","omen","ruckus","viktor"],
                    ["flavio","roberto","winston","lucio","ruckus","ruckus","viktor"],
                    ["carlitox","fernando","winston","lucio","omen","ruckus","d.va"],
                    ["claudia","alejo","winston","lucio","omen","ruckus","viktor"]
                    ]
    print(un_responsable_por_turno(matriz_horaria))
    
    pacientes = ["perro","gato","perro","perro","gato","perro","perro","perro","perro","gato"]
    print(subsecuencia_mas_larga(pacientes))