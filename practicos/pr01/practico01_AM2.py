nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 
sexos = ["f","f","m","f","m","f","m"]
fechas = [
"02/05/1943",
"07/09/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]

# nombre = "Santamaría, Carlos"
# nombre = "Hudson, Kate"

# Solución con find
# posComa = nombre.find(',')
# apellido = nombre[0:posComa]
# inicial = nombre[posComa + 2]
# print(inicial + '. ' + apellido)

# Solución con split
# nombreYapellido = nombre.split(', ')
# inicial = nombreYapellido[1][0]
# apellido = nombreYapellido[0]
# print(inicial + '. ' + apellido)

print('1)')
for nombre in nombres:
    nombreYapellido = nombre.split(', ')
    nombrePila = nombreYapellido[1]
    inicial = nombrePila[0]
    apellido = nombreYapellido[0]
    print(inicial + '. ' + apellido)

print('2)')
nombreLargo = ''
for nombre in nombres:
    posComa = nombre.find(',')
    nombrePila = nombre[posComa + 2:]
    if len(nombrePila) > len(nombreLargo):
        nombreLargo = nombrePila
print('El nombre más largo es', nombreLargo)

print('3)')
# for sexo in sexos:
#     if sexo == 'f':
#         print('chica')

cM = 0
dH = 19
mH = 5
aH = 2023
acumEdades = 0
for indice in range(len(sexos)):
    if sexos[indice] == 'f':
        cM += 1
        fecha = fechas[indice]
        # Corto fecha con slicing
        # dN = int(fecha[:2])
        # mN = int(fecha[3:5])
        # aN = int(fecha[6:])

        # Corto fecha con split
        dN, mN, aN = fecha.split('/')
        dN = int(dN)
        mN = int(mN)
        aN = int(aN)
        edad = aH - aN
        if (mN > mH) or (mN == mH and dN > dH):
            edad -= 1
        acumEdades += edad
print('El promedio de edad de las mujeres es', acumEdades // cM)
