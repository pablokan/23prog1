nombres = []
sexos = []

for i in range(3):
    nombre = input('Nombre: ')
    nombres.append(nombre)
    sexo = input('Sexo: ')
    sexos.append(sexo)
mujeres = []
for x in range(len(sexos)):
    if sexos[x] == 'f':
        mujeres.append(nombres[x])
print(mujeres)
