def imprimir_pares() -> None:
    i = 10
    while i <= 40:
        if i % 2 == 0:
            print(i)
            i += 2
        else:
            i += 1


imprimir_pares()