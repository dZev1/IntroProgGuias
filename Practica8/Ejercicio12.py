from queue import LifoQueue as Pila

def evaluar_expresion(s: str) -> float:
    operadores: list[str] = ["+", "-", "*", "/"]
    pila_operandos: Pila[int] = Pila()
    op1: float
    op2: float
    resultado: float
    
    for i in s:
        if (i not in operadores) and (i != " "):
            pila_operandos.put(int(i))
        if i in operadores:
            op2 = pila_operandos.get()
            op1 = pila_operandos.get()
            if i == "+":
                resultado = op1 + op2
            if i == "-":
                resultado = op1 - op2
            if i == "*":
                resultado = op1 * op2
            if i == "/":
                resultado = op1 / op2
            pila_operandos.put(resultado)
    return resultado

expresion: str = "3 4 + 5 * 2 -"

resultado: float = evaluar_expresion(expresion)

if __name__ == "__main__":
    print(resultado)