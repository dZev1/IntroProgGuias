def aprobado(notas: list[int]) -> int:
    length: int = len(notas)
    suma_de_notas: int = 0
    promedio: int = 0
    contador: int = 0
    resultado: int = 0
    
    for nota in notas:
        if nota >= 4:
            suma_de_notas += nota
            contador += 1
        if nota < 4:
            resultado = 3
            return resultado
        
    promedio = suma_de_notas / length
    
    if promedio >= 7 and contador == length:
        resultado = 1
    else:
        resultado = 2
    
    return resultado
    


calificaciones: list[int] = [4,4,4,4,4,4,4]

if __name__ == "__main__":
    print(aprobado(calificaciones))