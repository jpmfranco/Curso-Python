import math as m
def turno_farmacia():
    i = 0
    while True:
        i+=1
        yield f"F-{i}"

def turno_perfumeria():
    i = 0
    while True:
        i+=1
        yield f"P-{i}"

def turno_cosmetica():
    i = 0
    while True:
        i+=1
        yield f"C-{i}"

p = turno_perfumeria()
c = turno_cosmetica()
f = turno_farmacia()       

def decorardor_turno(letra):
        print("-"*10)
        print("Su turno es:  ")
        if letra == "P": 
           print(next(p))
        elif letra == "C":
            print(next(c))
        else:
            print(next(f))
        print("""Aguarde y 
sera atendido
                """)
        print("-"*10)

