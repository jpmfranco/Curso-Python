mi_archivo = open('Prueba.txt')

#print(mi_archivo.read())
#una_linea = mi_archivo.readline()
# una_linea = mi_archivo.readline()
# print(una_linea.upper())
# una_linea = mi_archivo.readline()
# print(una_linea)
# una_linea = mi_archivo.readline()
# print(una_linea)
# for l in mi_archivo:
#     print("Aqui dice: "+l)
todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)










mi_archivo.close()