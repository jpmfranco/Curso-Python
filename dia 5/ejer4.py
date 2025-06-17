def contar_primos(n):
    if n < 2:
        return 0
    primos = 0
    listprim = []
    j = 2
    count = 0
    while j < n+1:
        count = 0
        for i in range(2,n+1):
            if count > 1:
                break
            if j % i == 0:
                count+=1
            if count == 1 and i == n:
                primos+=1
                listprim.append(j)
        j+=1
    print(primos)
    return listprim

print(contar_primos(1))


    