def devolver_el_doble_si_es_par(n: int) -> int:
    if n % 2 == 0:
        return 2 * n
    else:
        return n
    
def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if n % 2 == 0:
        return n
    else:
        return n + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
    if n % 9 == 0:
        return 3 * n
    if n % 3 == 0:
        return 2 * n
    else:
        return n

def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
def elRango(n: float) -> str:
    if 10 <= n <= 20:
        return "Entre 10 y 20"
    if n < 5:
        return "Menor que 5"
    if n > 20:
        return "Mayor que 20"

def tiene_que_ir_de_vacaciones(sexo: str, edad:int) -> str:
    es_hombre_jubilado: bool = sexo == 'M' and edad >= 65
    es_mujer_jubilada: bool = sexo == 'F' and edad >= 60
    es_menor = edad < 18
    if es_hombre_jubilado or es_mujer_jubilada or es_menor:
        return "Anda de vacaciones"
    else:
        return "Te toca trabajar"
    

if __name__ == "__main__":
    x = 2
    x = devolver_el_doble_si_es_par(x)

    y = 3
    y = devolver_valor_si_es_par_sino_el_que_sigue(y)

    z = 6
    z = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(z)

    print('Diego,', lindo_nombre("DIEGO"))
    print('Agustina,', lindo_nombre("AGUSTINA"))
    print('Ana,', lindo_nombre("ANA"))
    
    print(tiene_que_ir_de_vacaciones('M', 15))