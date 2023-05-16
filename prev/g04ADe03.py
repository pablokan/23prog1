nombres = ['Ana', 'José', 'Lisa', 'Juan']
direcciones = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']
callesUnicas = []
cuentoCalles = []
personas = []

for i in range(len(direcciones)):
    p = 0
    while direcciones[i][p] != ' ':
        p -= 1
    calle = direcciones[i][:p]

    if calle not in callesUnicas:
        callesUnicas.append(calle)
        cuentoCalles.append(1)
        personas.append([nombres[i]])

    else:
        j = 0
        while calle != callesUnicas[j]:
            j += 1
        cuentoCalles[j] += 1
        personas[j].append(nombres[i])


for i in range(len(callesUnicas)):
    print(callesUnicas[i], cuentoCalles[i], personas[i])
