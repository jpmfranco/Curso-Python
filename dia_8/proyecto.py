import Proyectonumeros as p
from os import system
def menu():
    
    turno = True
    opcion = 0
    while turno:
        print("""A cual de las areas deseas ir:\n[1]- Perfumeria
[2]- Farmacia
[3]- Cosmeticos""")
        try:
            opcion = int(input())
        except :
            print("Error, elige un numero valido")
        else:
           if opcion == 1:
               dec = p.decorardor_turno("P")       
           elif opcion == 2:
               dec = p.decorardor_turno("F")
           elif opcion == 3:
               dec = p.decorardor_turno("C")
           print("¿Otro turno?\n[1]-Si\n[2]-No")
           opc = int(input())
           if opc == 1:
               system("cls")
           else:
               print("Adios!")
               system("pause")
               system("cls")
               turno = False
menu()