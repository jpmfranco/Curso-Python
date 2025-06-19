import time
import timeit

def prueba_for(numero):
    lista =  []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador +=1
    return lista

# inicio = time.time()
# prueba_for(10)
# final = time.time()
# print(final - inicio)

# inicio = time.time()
# prueba_while(10)
# final = time.time()
# print(final - inicio)
declaracion = """
prueba_for(10)
"""

setup = """
def prueba_for(numero):
    lista =  []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""
duracion = timeit.timeit(declaracion,setup,number = 1000000)
print(duracion)

declaracion2 = """
prueba_while(10)
"""

setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador +=1
    return lista
"""
duracion2 = timeit.timeit(declaracion2,setup2, number = 1000000)
print(duracion2)

