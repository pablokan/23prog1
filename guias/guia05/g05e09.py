enteros = [11, 3, 22]

def promedio(lista):
    t = 0
    for e in lista:
        t += e
    return t / len (lista)

def mayorQue(lista, valor):
    for e in lista:
        if e > valor:
            print(e)

p = promedio(enteros)
print('El promedio es', p)
mayorQue(enteros, p)

