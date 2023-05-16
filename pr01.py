# start 22:33
# end 22:54
nombresCompletos = [
'Torres, Ana',
'Hudson, Kate',
"Quesada, Benicio",
'Campoamores, Susana', 
'Santamaría, Carlos', 
'Skarsgard, Azul', 
'Catalejos, Walter' 
]

sexos = [
    'f',
    'f',
    'm',
    'f',
    'm',
    'f',
    'm'
]

fechasNac = [
    '02/05/1943',
    '07/09/1984',
    '10/02/1971',
    '21/12/1967',
    '30/01/1982',
    '30/08/1995',
    '18/07/1959',
]

# 0. Separo nombres y apellidos en dos listas
nombres = []
apellidos = []
for nombreCompleto in nombresCompletos:
    posComa = nombreCompleto.find(',')
    apellido = nombreCompleto[:posComa]
    nombre = nombreCompleto[posComa+2:]
    apellidos.append(apellido)
    nombres.append(nombre)

# 1. Inicial y Apellido 'Torres, Ana'  ---> 'A. Torres'
for i in range(len(nombres)):
    inicial = nombres[i][0]
    print(inicial + '. '+ apellidos[i])

# 2. El nombre más largo
nombreMasLargo = ''
for nombre in nombres:
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre
print(nombreMasLargo)

# 3. Promedio de edad de las mujeres
dH = 15
mH = 5
aH = 2023
acum = 0
cM = 0
for i in range(len(sexos)):
    if sexos[i] == 'f':
        cM += 1
        dN, mN, aN = fechasNac[i].split('/')
        dN =int(dN)
        mN =int(mN)
        aN =int(aN)
        edad = aH - aN
        if (mN > mH) or ((mN == mH) and (dN > dH)):
            edad -= 1
        print(edad)
        acum += edad
print(acum/cM)