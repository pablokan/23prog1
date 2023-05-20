direcciones = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']

calles = []
cantidades = []
for direccion in direcciones:
    posi = -1
    while direccion[posi] != ' ':
        posi -= 1
    calle = direccion[:posi]
    if calle not in calles:
        calles.append(calle)
        cantidades.append(1)
    else:
        i = 0
        while calles[i] != calle:
            i += 1
        cantidades[i] += 1

for x in range(len(calles)):
    print(calles[x], cantidades[x])



