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
print('Iniciales y apellidos de las personas:')
for nombre in nombres:
    posComa = nombre.find(',')
    inicialNombre = nombre[posComa+2:posComa+3]
    apellido = nombre[:posComa]
    print(inicialNombre + '.' + ' ' + apellido)
listaNueva = []
for nombre in nombres:
    posComa = nombre.find(',')
    inicialNombre = nombre[posComa+2:]
    listaNueva.append(inicialNombre)
masLargo = 0
nombreMasLargo = ''
for nombre in listaNueva:
    if len(nombre) > masLargo:
        nombreMasLargo = nombre
        masLargo = len(nombre)
print('El nombre mas largo es:', nombreMasLargo)
anioActual = 2023
mesActual = 5
diaActual = 17
sumaEdad = 0
for fecha in fechas:
    diaNac = int(fecha[0:2])
    mesNac = int(fecha[3:5])
    anioNac = int(fecha[6:11])
    edad = anioActual - anioNac
    if (mesNac > mesActual) or (mesNac == mesActual and diaNac > diaActual):
        edad -= 1
    sumaEdad = sumaEdad + edad 
promEdad = int(sumaEdad/len(fechas))
print('El promedio de edad de las mujeres es:', promEdad)
        
