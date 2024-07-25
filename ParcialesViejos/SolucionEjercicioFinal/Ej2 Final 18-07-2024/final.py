def cantidadApariciones(l: list[int], n: int) -> int:
    counter: int = 0
    for num in l:
        if n == num:
            counter += 1
    return counter

def transponer(m: list[list[int]]) -> list[list[int]]:
    columna: list[int] = []
    res: list[list[int]] = []
    for i in range(len(m)):
        columna = []
        for j in range(len(m)):
            columna.append(m[j][i])
        res.append(columna)
    return res
            

def esSudokuValido(m: list[list[int]]) -> bool:
    m_transposed: list[list[int]] = transponer(m)
    for i in range(len(m)):
        for n in range(1,10):
            if cantidadApariciones(m[i], n) > 1 or cantidadApariciones(m_transposed[i], n) > 1:
                return False
            # n += 1
    return True

if __name__ == "__main__":
    m_0 = [
        [1,2,3,4,5,6,7,8,9],
        [9,3,7,6,4,5,3,2,1],
        [0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,4,0,0,0],
        [0,0,0,0,6,0,0,0,0],
        [0,0,0,5,0,0,0,0,0],
        [0,0,4,0,0,0,0,0,0],
        [0,3,0,0,0,0,0,0,0],
        [2,0,0,0,0,0,0,0,0]
    ]
    m_1 = [
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,4,5,3,2,1],
        [0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,4,0,0,0],
        [0,0,0,0,6,0,0,0,0],
        [0,0,0,5,0,0,0,0,0],
        [0,0,4,0,0,0,0,0,0],
        [0,3,0,0,0,0,0,0,0],
        [2,0,0,0,0,0,0,0,0]
    ]
    print(esSudokuValido(m_0))
    print(esSudokuValido(m_1))
    
    
# [[1,2,3,4,5,6,7,8,9],[9,3,7,6,4,5,3,2,1],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,4,0,0,0],[0,0,0,0,6,0,0,0,0],[0,0,0,5,0,0,0,0,0],[0,0,4,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,0]]
# [[1,2,3,4,5,6,7,8,9],[9,8,7,6,4,5,3,2,1],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,4,0,0,0],[0,0,0,0,6,0,0,0,0],[0,0,0,5,0,0,0,0,0],[0,0,4,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,0]]