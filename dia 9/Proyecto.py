import os
import time
from datetime import date
import re
import math
from pathlib import Path

ruta = Path("C:\\Users\\pablo\\Documents\\GitHub\\Curso-Python\\dia 9\\Dia9proyecto\\Mi_Gran_Directorio") 


# shutil.unpack_archive('ProyectoDia9.zip','Dia9proyecto','zip')

def time_():
    hoy = date.today()
    print(f"Fecha de búsqueda: [{hoy.day}/{hoy.month}/{hoy.year}]")

def num_serie():
    archi = []
    numser = []
    patron = r'N\D{3}-\d{5}'
    for carp,subcarpeta,archivo in os.walk(ruta):
            for arc in archivo:
                arch = open(Path(carp,arc),'r')
                texto = arch.read()
                busqueda = re.search(patron,texto)
                if busqueda:
                    num = busqueda.group()
                    numser.append(num)
                    archi.append(arc)
    return archi, numser


def Show():
    print("-"*50)
    time_()
    inicio = time.time()
    arc, num = num_serie()
    final = time.time()
    print("ARCHIVO\t\tNRO. SERIE")
    print("-"*7+'\t\t'+'-'*10)
    i = 0
    while i <len(arc):
        print(f"{arc[i]}\t{num[i]}")
        i+=1
    print(f"Números encontrados: {len(arc)}")
    print(f"Duracion de la busqueda: {math.ceil(final-inicio)} segundos")
    print("-"*50)




Show()


