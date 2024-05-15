def peso_pino(height: int) -> int:
    if height <= 3:
        return height * 300
    else:
        return 2 * 100 * (height - 3) + 900

def es_peso_util(peso: int) -> bool:
    return peso >= 400 and peso <= 1000

def sirve_pino(height: int) -> bool:
    return es_peso_util(peso_pino(height))

if __name__ == '__main__':
    print(sirve_pino(5))