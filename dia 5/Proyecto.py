from random import choice

letras = "abcdefghijklmnopqrstuvwxyz"
listletras = []
listpalabras = ["gano","herramienta","martillo","equipo","sandwich","pantalla"]
lives = 6
pi = []
p = []
aciertos = 0
palabra_elegida = choice(listpalabras)
countword = len(palabra_elegida)
pal = [x for x in palabra_elegida]

def pedir_letra():
    print("\n" +"-" * 50 + "\n")
    letra  = input("Dame una letra: ").lower()
    print("\n" +"-" * 50 + "\n")
    letras_unicas = len(set(palabra_elegida))
    return letra,letras_unicas

def validar_letra(letra):
    for i in letras:
        if i == letra and letra not in  listletras:
            return True
    return False
        
def chequear_letra(letra,palabra, aciertos):
    Try = 0
    countword = 0
    if letra in palabra and letra not in p:
        p.append(letra)
        countword+=1
        aciertos+=1
    elif letra in palabra and letra in p:
        print("Esa palabra ya la elegiste, elige otra")
    else:
        pi.append(letra)
        Try = 1
    return Try,countword, aciertos

def show_word(palabra):
    lista_oculta = []
    for i in palabra:
        if i in p:
            lista_oculta.append(i)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))


i = 0
a = 0
print("------|Bienvenido al juego del ahorcado|------")
print("----------------------------------------------")
print("\n")
print("Adivina la palabra....")
while  lives > 0:
    print("\n" +"-" * 50 + "\n")
    show_word(palabra_elegida)
    print(f"Vidas: {lives}")
    letra,letras_unicas = pedir_letra()
    if(validar_letra(letra)):
        Try, check, aciertos = chequear_letra(letra,palabra_elegida,aciertos)
        if aciertos < letras_unicas:
            
            if Try != 1 and check > 0:
                countword-=1
            else:
                print("Esa letra no esta en la palabra")
                lives-=1
        else:
            show_word(palabra_elegida)
            print("\n" +"-" * 50 + "\n")
            print("Ganaste, muchas felicidades")
            print("\n" +"-" * 50 + "\n")
            break
        
    else:
      print("-------------------------------------------------")
      print("letra no existe vuelve a escribir una letra valida")
      print("-------------------------------------------------")

      continue
else:
    if lives == 0:
        print("\n")
        print("-------------------------------------------------")
        print("Lo siento perdiste, la palabra era: " + palabra_elegida)
    print("-------------------------------------------------")
    print("Fin del juego")
    print("-------------------------------------------------")





    




