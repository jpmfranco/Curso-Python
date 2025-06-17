from pathlib import Path
from os import system
import os

nombre = input("Dame el nombre de la categoria: ")
ruta  = Path(Path.home(),"Recetas",nombre)
Ruta = os.makedirs(ruta)
print(Ruta)