txt = input("Ingresa cualquier texto: ").lower()
print("\n")
lista = []
lista.append(input("Ingresa la primer letra: ").lower())
lista.append(input("Ingresa la segunda letra: ").lower())
lista.append(input("Ingresa la tercera letra: ").lower())
print(f"La cantidad de veces que aparece la primer letra es: {txt.count(lista[0])},\n la segunda es: {txt.count(lista[1])} y \nla tercera es {txt.count(lista[2])}")
print("\n")
lt = txt.split()
print(f"La cantidad de palabras que hay son {len(lt)}")
print("\n")
print(f"La primera letra del texto es {txt[0]} y la ultima es {txt[-1]}")
print("\n")
lt.reverse()
lisrev = " ".join(lt)
print(f"Aqui tienes la lista en reversa: {lisrev}")
print("\n")
dic = {False: 'no', True:'si'}
print(f"La palabra python {dic['python' in txt]} esta en el texto")


