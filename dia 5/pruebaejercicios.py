import random 
def lanzarmoneda():
    return random.choice(["Cara", "Cruz"]) 

def probarsuerte(resultado,lista):
    if resultado == "Cara":
        print("La lista se autodestruirá")
        lista.clear()
        return lista
    else:
        print("La lista fue salvada")
        return lista
    