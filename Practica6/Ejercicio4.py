def peso_pino(height: int) -> int:
    altura_centimetros: int = height * 100
    peso: int
    if height <= 3:
        peso = altura_centimetros * 3
        return peso
    else:
        peso = 2 * (altura_centimetros - 300) + 900
        return peso

def es_peso_util(peso: int) -> bool:
    return peso >= 400 and peso <= 1000

def sirve_pino(height: int) -> bool:
    return es_peso_util(peso_pino(height))

if __name__ == '__main__':
    print(sirve_pino(5))