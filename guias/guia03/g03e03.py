nombres = []
sexos = []
for i in range(8):
    nombre = input('Nombre: ')
    sexo = input('Sexo (m/f): ')
    nombres.append(nombre)
    sexos.append(sexo)

mujeres = []
for x in range(8):
    if sexos[x] == 'f':
        mujeres.append(nombres[x])

print('Lista de mujeres: ', mujeres)
