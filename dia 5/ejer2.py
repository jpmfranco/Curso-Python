def cualquiera(palabra):
    pal = []
    for i in palabra:
        pal.append(i)
    pal.sort()
    print(pal)
    for letra in pal:
        j = pal.index(letra)
        while j < len(pal) - 1:
            j += 1 
            if pal[j] == letra:
                print("La letra se puede eliminar")
                pal.pop(j)
                break
            else:
                print("No se puede eliminar la letra")
    return pal

print(cualquiera("amargo"))