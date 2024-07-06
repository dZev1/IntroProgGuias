
# Ejercicio promedio de salidas
def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
  res: dict[str, tuple[int, float]] = {}
  for clave in registro:
    salas_escapadas:list[int] = salas_con_salidas(registro[clave])
    cantidad_salidas:int = len(salas_escapadas)
    promedio:float = promedio_salas(salas_escapadas)
    res[clave] = (cantidad_salidas, promedio)
  return res
 
def salas_con_salidas(tiempos_salidas:list[int]) -> list[int]:
  res:list[int] = []
  for elem in tiempos_salidas:
    if (elem > 0 and elem < 61):
      res.append(elem)
  return res
  
def promedio_salas(tiempos_salidas:list[int]) -> float:
  suma:int = 0
  res: float = 0.0
  for elem in tiempos_salidas:
    suma += elem
  if (suma > 0):
    res = (suma / len(tiempos_salidas))
  return res
  
  

# Ejercicio Tiempo más Rápido
def tiempo_mas_rapido (tiempos_salas: list[int])-> int:
  maximo_actual: int = tiempos_salas[0]
  res: int = 0
  for indice in range(len(tiempos_salas)):
    elem_actual = tiempos_salas[indice]
    if (elem_actual < maximo_actual and elem_actual < 61 and elem_actual > 0):
      res = indice
      maximo_actual = elem_actual
  return res
  
# Ejercicio rachas mas larga  
def racha_mas_larga (tiempos: list[int])-> tuple[int, int]:
  pos_menor:int = 0
  pos_mayor:int = 0
  cantidad_elementos_mayores:int = 0
  pos_menor_actual:int = -1
  cantidad_elementos_mayores_actual:int = 0
  
  for indice in range(len(tiempos)):
    elemento_actual = tiempos[indice]
    if (elemento_actual < 61 and elemento_actual > 0):
      cantidad_elementos_mayores_actual += 1
      if (pos_menor_actual == -1):
        pos_menor_actual = indice
    else:
      # si la racha actual es mas larga que la anterior la recuerdo
      # sino la olvido y vuelvo a contar desde ahora
      if (cantidad_elementos_mayores_actual > cantidad_elementos_mayores):
        cantidad_elementos_mayores = cantidad_elementos_mayores_actual
        cantidad_elementos_mayores_actual = 0
        
        pos_menor = pos_menor_actual
        pos_menor_actual = -1 # reinicio la pos_menor_actual
        
        pos_mayor = pos_menor + cantidad_elementos_mayores - 1 # resto 1 porque es posicion
  
  if (cantidad_elementos_mayores_actual > cantidad_elementos_mayores): # caso final de la secuencia
        cantidad_elementos_mayores = cantidad_elementos_mayores_actual
        pos_menor = pos_menor_actual
        pos_mayor = pos_menor + cantidad_elementos_mayores - 1 # resto 1 porque es posicion      
  
  return (pos_menor,pos_mayor)
  

def escape_en_solitario (amigos_por_salas: list[list[int]])-> list[int]:
  res:list[int] = []
  
  for indice in range(len(amigos_por_salas)):
    amigos_de_sala = amigos_por_salas[indice]
    primer_amigo = amigos_de_sala[0] == 0
    segundo_amigo = amigos_de_sala[1] == 0
    tercer_amigo = amigos_de_sala[2] != 0
    cuarto_amigo = amigos_de_sala[3] == 0
    if (primer_amigo and segundo_amigo and tercer_amigo and cuarto_amigo):
      res.append(indice)
    
  return res
