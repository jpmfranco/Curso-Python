from os import system
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"Cuenta: {self.numero_cuenta}\nNombre: {self.nombre} {self.apellido}\nBalance: {self.balance}"
    
    def depositar(self,cantidad):
        self.balance += cantidad
    
    def retirar(self,cantidad):
        self.balance -= cantidad

def crear_cliente(nombre,apellido, numero_cuenta, balance):
    clie = Cliente(nombre,apellido,numero_cuenta,balance)
    return clie

def datos():
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    num = int(input("Dime tu numero de cuenta: "))
    balance = int(input("Dame tu balance de cuenta: "))
    return nombre, apellido, num, balance

def inicio():
    nombre,apellido,num, balance = datos()
    cliente = crear_cliente(nombre, apellido, num, balance)
    system("cls")
    terminado = False
    while not terminado:
        print("-"*20+f'|Bienvenido al cajero|'+'-'*20)
        print("""
            ¿Que opcion eliges?
              [1] - Depositar
              [2] - Retirar
              [3] - Salir
            Opcion elegida:     
        """)
        opcion = int(input("\t"))
        print("-"*80)
        if opcion == 1:
            system("cls")
            cant = int(input("Dime la cantidad a depositar:"))
            cliente.depositar(cant)
            print(cliente)
            system("pause")
            system("cls")
        elif opcion == 2:
            system("cls")
            cant = int(input("Dime la cantidad a retirar: "))
            if cant <= cliente.balance:
                cliente.retirar(cant)
                print(cliente)
                system("pause")
                system("cls")
            else:
                print("La cantidad a retirar excede la cantidad total de tu balance")
                system("pause")
                system("cls")
        elif opcion == 3:
            system("cls")
            print("Has salido del cajero....")
            terminado = True
        else:
            
            print("Error, ese numero no esta en las opciones")

inicio()
