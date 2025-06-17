from pathlib import Path
from os import system
import os
ruta = Path(Path.home(),"Recetas")
listacat = [c.name for c in ruta.glob("**") if c != ruta]
#leer recetas
def elegir_categoria(): 
    band = True
    while band:
        print("Categorias: \n")
        print('-'+'\n-'.join(listacat))
        print("-"*65)
        eleccion = input("¿Que categoria eliges (Pon el nombre correcto): ").capitalize()
        if eleccion in listacat:
            band = False
        else:
            print("no existe esa categoria elige correctamente")
            system("pause")
            system("cls")
    return eleccion

def mostrar_recetas(categoria):
    ruta = Path(Path.home(),"Recetas",categoria)
    print("-"*65)
    print("Recetas: ")
    for txt in Path(ruta).glob("*.txt"):
        print(txt.stem)
    print("-"*65)
    

def elegir_receta():
    eleccion = input("¿Que receta quieres?(Si no hay recetas da enter) ")
    return eleccion
    

def leer_receta(receta,categoria):
    ruta = Path(Path.home(),"Recetas",categoria,receta+'.txt')
    if ruta.exists():
        print("-"*65)
        print(f"Receta:")
        print(ruta.read_text())
        print("-"*65)
        system("Pause")
        system("cls")

    else:
        print(receta)
        if receta  == '':
            print("No existen recetas")
            system("Pause")
            system("cls")
        else:
            print("Dame bien el nombre de la receta")
            system("Pause")
            system("cls")


#crear receta
def nombre_contenido(categoria):
    nombre = input("Dame el nombre de la receta: ")
    contenido = input("Dame el contenido de la receta: ")
    ruta = Path(Path.home(),"Recetas",categoria,nombre+'.txt')
    archivo = open(ruta,'w')
    archivo.write(contenido)
    archivo.close()
    print("Receta creada con exito!")


#crear categoria
def crear_categoria(): # nombre
    nombre = input("Dame el nombre de la categoria: ")
    ruta  = Path(Path.home(),"Recetas",nombre)
    Ruta = os.makedirs(ruta)
    listacat.append(nombre.capitalize())
    print(Ruta)
  

#eliminar recetas
def eliminar_receta(receta,categoria):
    ruta = Path(Path.home(),"Recetas",categoria,receta+'.txt')
    if ruta.exists():
        ruta.unlink()
        print("Se elimino la receta")
    else:
        print("No existe el archivo")

#eliminar categoria
def eliminar_categoria(categoria):
    ruta = Path(Path.home(),"Recetas",categoria)
    if ruta.exists():
        for archivo in ruta.iterdir():
            if archivo.is_file():
                archivo.unlink()
        ruta.rmdir()
        listacat.remove(categoria)
        print("Categoria eliminada con exito")
    else:
        print("No existe esa categoria")

terminado = False
while terminado == False:
    print("-"*20+'|Bienvenido al recetario|'+'-'*20)
    ruta = Path(Path.home(),"Recetas")
    print(f"Las recetas se encuentran en: {ruta}")
    count = 0
    for r in ruta.glob("**/*.txt"):
        count+=1
    print(f"Tienes {count} recetas")
    print("-"*65)
    opcion = int(input("Elige una opcion del siguiente menu(Solo numero): \n[1] - Leer receta\n[2] - Crear" \
    " receta\n[3] - Crear categoria\n[4] - Eliminar receta\n[5] - Eliminar categoria\n" \
    "[6] - Finalizar programa\nRespuesta: "))
    print("-"*65)
    system("cls")
    if opcion == 1:
        categoria = elegir_categoria()
        mostrar_recetas(categoria)
        receta = elegir_receta()
        leer_receta(receta,categoria)
    elif opcion == 2:
        categoria = elegir_categoria()
        nombre_contenido(categoria)
    elif opcion == 3:
        crear_categoria()
        system("Pause")
        system("cls")

    elif opcion == 4:
        categoria = elegir_categoria()
        mostrar_recetas(categoria)
        receta = elegir_receta()
        eliminar_receta(receta,categoria)
        system("Pause")
        system("cls")
    elif opcion == 5:
        categoria = elegir_categoria()
        eliminar_categoria(categoria)
        system("Pause")
        system("cls")
    elif opcion == 6:
        print("Nos vemos vuelve, pronto a tu recetario!")
        terminado = True
    else:
        print("Error de eleccion, elija de nuevo...")
else:
    print("Error de numero")
