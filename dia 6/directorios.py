from pathlib import Path

carpeta = Path("/Users/pablo/Documents/Semestre/curso python/dia 6") / "otroarchivo.txt"
# archivo = carpeta / "otroarchivo.txt"

mi_archivo = open(carpeta)
print(mi_archivo.read())

# ruta = "C:\\Users\\pablo\\Documents\\Semestre\\curso python\\dia 6\\Prueba.txt"

# elemento  = os.path.basename(ruta)
# elemento  = os.path.dirname(ruta)
# elemento  = os.path.split(ruta)
# os.rmdir("C:\\Users\\pablo\\Documents\\proyecto github\\otra")

# otro  = open("C:\\Users\\pablo\\Documents\\proyecto github\\otroarchivo.txt")
# print(otro.read())
