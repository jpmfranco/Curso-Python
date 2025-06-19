import Proyectonumeros as p

def menu():
    dec = p.decorardor_turno()
    turno = True
    opcion = 0
    while turno:
        print("""A cual de las areas deseas ir:\n[1]- Perfumeria
              [2]- Farmacia
              [3]- Cosmeticos""")
        opcion = int(input())
        if opcion == 1:
            dec(p.turno_perfumeria)
        elif opcion == 2:
            dec(p.turno_farmacia)