import math as m
def turno_farmacia():
    for i in range(100000):
        yield f"F-{i+1}"

def turno_perfumeria():
    for i in range(100000):
        yield f"P-{i+1}"

def turno_cosmetica():
    for i in range(100000):
        yield f"C-{i+1}"

def decorardor_turno(funcion):
    
    def subfuncion():
        print("Su turno es:  ")
        print(next(funcion()))
        print("""Aguarde y 
sera atendido
                """)
    return subfuncion


