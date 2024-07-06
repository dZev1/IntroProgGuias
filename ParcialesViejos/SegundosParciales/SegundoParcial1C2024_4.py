from queue import Queue as Cola

# Ej 1
def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    urgentes_aux: Cola[int] = Cola()
    postergables_aux: Cola[int] = Cola()
    res: Cola[int] = Cola()
    
    while not(urgentes.empty() and postergables.empty()):
        elem = urgentes.get()
        res.put(elem)
        urgentes_aux.put(elem)
        
        elem = postergables.get()
        res.put(elem)
        postergables_aux.put(elem)
    
    while not(urgentes_aux.empty() and postergables_aux.empty()):
        elem = urgentes_aux.get()
        urgentes.put(elem)
        elem = postergables_aux.get()
        postergables.put(elem)

    return res

# Ej 2
def cant_apariciones(elem: str, lista: list[str]) -> int:
    res: int = 0
    for i in lista:
        if elem == i:
            res += 1
    return res

def alarma_epidemiologica(registros: list[tuple[int,str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    enfermedades_registros: list[str] = []
    res: dict[str, float] = {}
    
    if registros == []:
        return {}
    
    for paciente in registros:
        if paciente[1] in infecciosas:
            enfermedades_registros.append(paciente[1])
    
    for enfermedad in enfermedades_registros:
        porcentaje_enfermedad = (cant_apariciones(enfermedad,enfermedades_registros) / len(registros))
        if  porcentaje_enfermedad >= umbral:
            res[enfermedad] = porcentaje_enfermedad
    
    return res
    
# Ej 3
def maximum(lista: list[int]) -> int:
    curr_max: int = lista[0]
    for i in lista:
        if i > curr_max:
            curr_max = i
    return curr_max

def empleados_del_mes(horas: dict[int,list[int]]) -> list[int]:
    lista_horas_totales: list[int] = []
    res: list[int] = []
    total_horas: int = 0
    diccionario_aux: dict[int, int] = {}
    
    for id in horas.keys():
        diccionario_aux[id] = 0
        
    for id_empleado in horas.keys():
        total_horas = 0
        for i in horas[id_empleado]:
            total_horas += i
        lista_horas_totales.append(total_horas)
        diccionario_aux[id_empleado] = total_horas
    
    maximo_horas = maximum(lista_horas_totales)

    for id in diccionario_aux.keys():
        if diccionario_aux[id] == maximo_horas:
            res.append(id)
    return res

# Ej 4
def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = []
    total_camas_por_piso = len(camas_por_piso[0])
    contador_camas_ocupadas:int
    
    for piso in camas_por_piso:
        contador_camas_ocupadas = 0
        for esta_ocupada in piso:
            if esta_ocupada:
                contador_camas_ocupadas += 1
        res.append(contador_camas_ocupadas / total_camas_por_piso)
    return res



if __name__ == "__main__":
    regs = [(787,"fan de rosalia"), (943, "ricotero"), (9635, "otaku"), (232, "otaku"), (787,"fan de dillom"), (943, "ricotero"), (123, "otaku"), (231,"fan de dillom")]
    infecs = ["ricotero", "fan de dillom", "otaku"]
    umbr = 0.3
    #print(alarma_epidemiologica(regs,infecs,umbr))
    
    empleados_horas = {
                       12321: [8,6,8,8,5,0,0,8,7,0,0,0,6],
                       23212: [8,8,6,8,5,0,0,8,7,0,0,0,6],
                       12329: [8,6,8,8,5,0,0,0,5,0,0,0,3],
                       12322: [0,9,8,8,5,0,10,0,5,0,0,0,3]
                       }
    #print(empleados_del_mes(empleados_horas))
    
    hospital_camas = [
                    [True, False, False, False, True, True],
                    [False, False, False, False, False, True],
                    [True, False, True, False, True, True],
                    [True, True, True, True, True, True],
                    [True, False, False, False, True, True],
                    [False, False, False, False, False, False]
                     ]
    print(nivel_de_ocupacion(hospital_camas))