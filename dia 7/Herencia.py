class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        


    def nacer(self):
        print("Este animal ha nacido")



class Pajaro(Animal):
    pass

# print(Pajaro.__bases__) #bases is for say who is like his parent
# print(Animal.__subclasses__())#subclases like its name says is the sub class of the principal

piolin = Pajaro(2,"amarillo")

print(piolin.color)
