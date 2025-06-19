import os
# import send2trash
# import shutil
# print(os.getcwd())
# archivo = open('curso.txt','w')
# archivo.write('Texto de prueba')
# archivo.close()
# print(os.listdir())
# shutil.move('curso.txt','C:\\Users\\pablo\\Escritorio')
# print(os.walk("C:\\Users\\pablo\\Recetas"))


ruta = "C:\\Users\\pablo\\Recetas"

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f'En la carpeta {carpeta}')
    print(f"las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("los archivos son:")
    for arc in archivo:
        if arc.startswith("2015"):
            print(f"\t{arc}")
    print("\n")