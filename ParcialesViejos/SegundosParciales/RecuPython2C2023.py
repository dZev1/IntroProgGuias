# Auxiliares
def minimo(lista: list[float]) -> float:
    curr_minimo = lista[0]
    
    for numero in lista:
        if numero < curr_minimo:
            curr_minimo = numero

    return curr_minimo

def maximo(lista: list[float]) -> float:
    curr_maximo = lista[0]
    
    for numero in lista:
        if numero > curr_maximo:
            curr_maximo = numero

    return curr_maximo

def cant_apariciones(num: int, lista: list[int]) -> int:
    contador: int = 0
    for i in lista:
        if i == num:
            contador += 1
    return contador

# Ejercicio 1
def cantidad_ap_antes_corte(c: str, s: str) -> int:
    contador: int = 0
    for char in s:
        if char == c:
            contador += 1
        if char == "x":
            return contador
    return contador

def verificar_transacciones(s:str) -> int:
    res: int = (350 * cantidad_ap_antes_corte("r", s)) - (56 * cantidad_ap_antes_corte("v", s))

    while res < 0:
        res += 56
    
    return res

# Ejercicio 2


def valor_minimo(s: list[tuple[float, float]]) -> float:
    lista_primeras_pos: list[float] = []
    
    for item in s:
        lista_primeras_pos.append(item[0])
    
    return minimo(lista_primeras_pos)
    
# Ejercicio 3
def valores_extremos(cotizaciones_diarias: dict[str, list[tuple[int, float]]]) -> dict[str, tuple[float,float]]:
    res: dict[str,tuple[float,float]] = {}
    lista_valores: list[float] = []
    minimum: int = 0
    maximum: int = 0
    for clave in cotizaciones_diarias.keys():
        res[clave] = (0.0,  0.0)
    
    for key in res.keys():
        lista_valores = []
        for i in range(len(cotizaciones_diarias[key])):
            lista_valores.append(cotizaciones_diarias[key][i][1])
        
        minimum = minimo(lista_valores)
        maximum = maximo(lista_valores)
        
        res[key] = (minimum, maximum)
    return res
        

# Ejercicio 4
def  es_sudoku_valido(sudoku: list[list[int]]) -> bool:
    longitud:int = len(sudoku)
    res: bool = True
    for i in range(longitud):
        columna: list[int] = []
        for fila in sudoku:
            columna.append(fila[i])
        
        for numero in columna:
            if (cant_apariciones(numero, columna) > 1 or
                cant_apariciones(numero,sudoku[i]) > 1) and numero != 0:
                res = False
        
    return res

if __name__ == "__main__":
    historial = "ssrvvvvsvvsvvv"
    #print(verificar_transacciones(historial))
    temperaturas = [(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]
    #print(valor_minimo(temperaturas))
    cotizaciones =  {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
    #print(valores_extremos(cotizaciones))
    m = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 4, 5, 3, 2, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(es_sudoku_valido(m))
    