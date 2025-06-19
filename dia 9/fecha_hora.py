# import datetime
from datetime import datetime
from datetime import date

# mi_hora = datetime.time(17, 35)
mi_dia = datetime.date(2025,10,17)
print(mi_dia.today())
# print(mi_hora.hour)
mi_fecha = datetime(2025,5,15,22,10,15,2500)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)
nacimiento = date(1995,3,5)
defuncion = date(2095,6,19)

vida = defuncion - nacimiento
print(vida.seconds)
despierta = date(2002,7,5)
duerme =date(2025,6,19)

vigilia = duerme - despierta
days = vigilia.days
print(days/365)
