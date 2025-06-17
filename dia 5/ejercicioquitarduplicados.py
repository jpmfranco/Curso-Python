def reducir_lista(lista_numeros):
    for x in lista_numeros: 
        j = lista_numeros.index(x)
        while j < len(lista_numeros)-1:
            j += 1
            print(f"iteracion {j}")
            print(f"valor de x: {x}")
            print(f"index de x: {lista_numeros.index(x)}")
            print(f"valor de j: {lista_numeros[j]}")
            print(f"index de j: {j}")
            print(f"index de j: {lista_numeros.index(lista_numeros[j])}")

            if x == lista_numeros[j]:
                print(f"se elimina el valor {lista_numeros[j]} que estaba en la posicion {j}")
                print(lista_numeros.pop(j))
                print(lista_numeros)
            else:
                pass
        print(f"-----------------------------------------------")
               
    lista_numeros.pop(lista_numeros.index(max(lista_numeros)))
    
    return lista_numeros

def promedio(lista_numeros):
    suma = 0
    for i in lista_numeros:
        suma += i
    
    return suma/len(lista_numeros)

lista_numeros = [1,2,15,7,2]
Lista_numeros = reducir_lista(lista_numeros)
print(Lista_numeros) 
#print(promedio(lista_numeros))