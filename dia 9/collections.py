# from collections import Counter
# numeros = [8,6,5,4,3,3,2,65,6,4,2,2]
# frase = 'al pan pan y al vino vino'
# serie = Counter([1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3])
# # print(Counter(numeros))
# # print(Counter("mississippi"))
# print(Counter(frase))
# print(serie)
# from collections import defaultdict

# mi_dic = {'uno':'verde', 'dos':'azul','tres':'rojo'}
# print(mi_dic['cuatro'])
# mi_dic = defaultdict(lambda: 'nada')
# mi_dic['uno'] = 'verde'
# print(mi_dic['dos'])
from collections import namedtuple

Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)
