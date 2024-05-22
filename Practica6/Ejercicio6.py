def imprimir_numeros_1_al_10() -> None:
    i: int = 1
    while i <= 10:
        print(i)
        i += 1 

def imprimir_numeros_pares_10_40() -> None:
    i: int = 10
    while i <= 40:
        print(i)
        i += 2

def imprimir_eco_10_veces() -> None:
    i: int = 0
    while i < 10:
        print("eco")
        i += 1

def imprimir_cuenta_regresiva(limite_sup: int) -> None:
    i: int = limite_sup
    while i > 0:
        print(i)
        i += -1
    print("DESPEGUE!")

def monitorear_viaje_tiempo(yr_partida: int, yr_destino: int) -> None:
    i: int = yr_partida
    j: int = yr_destino

    while i > j:
        i += - 1
        print("Viajo un año al pasado, estamos en el año", i)

def linea() -> None:
    print("---------------------------------------")

if __name__ == "__main__":
    imprimir_numeros_1_al_10()

    linea()

    imprimir_numeros_pares_10_40()

    linea()

    imprimir_eco_10_veces()

    linea()

    imprimir_cuenta_regresiva(30)
    
    linea()
    
    monitorear_viaje_tiempo(2004,1980)


