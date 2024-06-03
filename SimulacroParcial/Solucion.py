# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s: list[int], e: int) -> int:
    longitud = len(s)
    
    for i in range(longitud - 1, -1, -1):
        if s[i] == e:
            return i
    
# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def pertenece(e: int, s: list[int]) -> bool:
    for elem in s:
        if e == elem:
            return True
    return False

def pertenece_a_ambas(e:int, s: list[int], t: list[int]) -> bool:
    return pertenece(e, s) and pertenece(e, t)

def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    res: list[int] = []
    st: list[int] = s + t
    
    for elem in st:
        if not(pertenece_a_ambas(elem,s,t)):
            res.append(elem)
    return res

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales (ing: dict, ale: dict):
    res: int = 0
    for palabra in ing.keys():
        if pertenece(palabra, ale.keys()) and ing[palabra] == ale[palabra]:
            res +=1
    return res

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def cantidad_apariciones(n: int, s: list[int]) -> int:
    res: int = 0
    for e in s:
        if e == n:
           res += 1
    return res

def convertir_a_diccionario(lista: list[int]) -> dict:
    diccionario: dict = {}
    for elem in lista:
        diccionario[elem] = cantidad_apariciones(elem, lista)
    return diccionario

lista = [-1,0,4,100,100,-1,-1]
print(convertir_a_diccionario(lista))