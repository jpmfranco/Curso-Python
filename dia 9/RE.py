import re
"""/d         digito numerico             v\d.\d\d
/w            caracter alfanumerico       \w\w\w-\w\w
/s            espacio en blanco           numero\s\d\d
/D            NO numerico                 \D\D\D\D
/W            NO alfanumerico             \W\W\W
/S            NO espacio blanco           \S\S\S\S  

cuantificadores
+             1 o mas veces               codigo_\d-\d+
{n}           se repite n veces           \d-\d{4}
{n,m}         se repite de n a m veces    \w{3,5}
{n,}          desde n hacia arriba        -\d{4,}-
*             0 o mas veces               \w\s*\w
?             1 o 0                       casas? 
"""
# texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

# palabra = 'ayuda' in texto
# print(palabra)

# patron = 'nada'

# busqueda = re.search(patron,texto) # solo una
# busqueda = re.findall(patron,texto) # varias palabra

# print(busqueda)
# texto = "llama al 564-4525-6588 ya mismo"
# patron = r'\d{3}-\d{3}-\d{4}'

# resultado = re.search(patron, texto)
# print(resultado)
# clave = input("Clave: ")

# patron = r'\D{1}\w{7}'

# chequear = re.search(patron,clave)
# print(chequear)
# texto  = "No atendemos los jueves por la tarde6"

# buscar = re.findall(r'[^\s]+',texto)
# buscar = re.search(r'.com$',texto)
# print(' '.join(buscar))
def verificar_email(email):
    patron = "@"
    busqueda = re.search(patron, email)
    busqueda2 = re.search(r'.\w.com$',email)
    if busqueda and busqueda2:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

verificar_email("example@gmail..com")