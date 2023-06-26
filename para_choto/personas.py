from datetime import date
lista = []
with open('personas.txt') as archPersonas:
    archPersonas.readline()
    for linea in archPersonas:
        fecha = linea.split()[1]
        d, m, a = [int(e) for e in fecha.split('/')]
        hoy = date.today()
        edad = hoy.year - a
        if (m > hoy.month) or (m == hoy.month and d > hoy.day):
            edad -= 1
        if edad >= 18:
            l = linea.split()[0] + str(edad) + '\n'
            lista.append(l)

with open('mayores.txt', 'w') as archMayores:
    archMayores.writelines(lista)

