# def cambiar_letras(tipo):

#     def mayuscula(texto):
#         print(texto.upper())


#     def miniscula(texto):
#         print(texto.lower())

#     if tipo == 'may':
#         return mayuscula
#     elif tipo == "min":
#         return miniscula
    
# operacion = cambiar_letras('may')
# operacion("palabra")
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayusculas)

mayuscula_decorada("Python")