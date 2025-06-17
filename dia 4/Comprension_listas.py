# palabra = 'python'
# lista = []
# for letra in palabra:
#     lista.append(letra)

# print(lista)
# palabra = 'python'
# lista = [n  for n  in range(0,21,2) if n % 2 == 0 and n != 0]
# lista = [n if n % 2 == 0 and n != 0 else 'no' for n  in range(1,21)]
# print(lista)
pies = [10,20,30,40,50]
metros= [round(n/3.281,2) for n in pies]
print(metros)


