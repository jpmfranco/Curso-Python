from pathlib import Path, PureWindowsPath

carpeta = Path("/Users/pablo/Documents/Semestre/curso python/dia 6/Prueba1.txt")
# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

rutawindows = PureWindowsPath(carpeta)
# if not carpeta.exists():
#     print("Este archivo no existe")
# else:
#     print("Genial, existe")
print(rutawindows)
