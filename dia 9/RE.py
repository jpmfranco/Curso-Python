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
texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = 'ayuda' in texto
print(palabra)

patron = 'nada'

busqueda = re.search(patron,texto)
print(busqueda)