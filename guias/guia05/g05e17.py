# Escribe una función que encuentre el número que más se repite en una lista.

lista = [11, 0, 22, 22, 0, 22, 1, 8, 5, 0, 32323, 0, 55555, 0]

def moreRep(l):
    noRepList = []
    q = []
    for n in l:
        if n not in noRepList:
            noRepList.append(n)
            q.append(1)
        else:
            i = noRepList.index(n)
            q[i] += 1
    print(noRepList, q)
    valor = l[q.index(max(q))]
    return valor, max(q)

print(moreRep(lista))

