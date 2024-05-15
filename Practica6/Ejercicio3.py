def es_nombre_largo(nombre : str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

def alguno_es_cero(n1: float,n2: float) -> bool:
    return n1 == 0 or n2 == 0

def es_bisiesto(yr: int) -> bool:
    return yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0)

if __name__ == '__main__':

    # alguno es cero
    print(alguno_es_cero(0,3))
    print(alguno_es_cero(3,0))
    print(alguno_es_cero(2,4))
 
    # es nombre largo
    print(es_nombre_largo("MATIAS"))
    print(es_nombre_largo("AL"))
    print(es_nombre_largo("DIEGARDOOO"))

    # es_bisiesto
    print(es_bisiesto(2000))
    print(es_bisiesto(1100))
    print(es_bisiesto(2004))

