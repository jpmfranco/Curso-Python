# class Animal:
    
#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
        

#     def nacer(self):
#         print("Este animal ha nacido")

#     def hablar(self):
#         print("Este animal emite un sonido")
    



# class Pajaro(Animal):
    
#     def __init__(self, edad, color, altura_vuelo):
#         # self.edad = edad
#         # self.color = color
#         # self.altura_vuelo = altura_vuelo
#         super().__init__(edad,color)
#         self.altura_vuelo = altura_vuelo
        


#     def hablar(self):
#         print("pio")
    
#     def volar(self, metros):
#         print(f"El pajaro vuela {metros} metros")


# piolin = Pajaro(3,"amarillo",60)
# mi_animal = Animal(5, 'negro')
# # piolin.nacer()
# piolin.hablar()
# piolin.volar(100)

class Padre:
    def hablar(self):
        print("Hola")

class Madre:

    def reir(self):
        print("ja ja")

    def hablar(self):
        print("que tal")

class Hijo(Padre,Madre): #if herency same method, first class herency will herency the method to the class
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()
print(Nieto.__mro__)# this is the hierarchy of herency