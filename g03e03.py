nombres = []
sexos = []

for x in range(3):
    nombre = input('Nombre: ')
    sexo = input('Sexo: ')
    nombres.append(nombre)
    sexos.append(sexo)
mujeres = []
for i in range(len(sexos)):
    if sexos[i] == 'f':
        mujeres.append(nombres[i])
print("Las mujeres son", mujeres)        


