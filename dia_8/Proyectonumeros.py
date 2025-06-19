import math as m
def turno_farmacia():
    for i in range(m.inf):
        yield f"F-{i}"

def turno_perfumeria():
    for i in range(m.inf):
        yield f"P-{i}"

def turno_cosmetica():
    for i in range(m.inf):
        yield f"C-{i}"

def decorardor_turno(funcion):
    print("Su turno es:  ")
    funcion()
    print("""Aguarde y
           sera atendido
            """)


