nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"] 
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]

nombresAux = ''
nombreMasLargo = ''

contador = 0 # contador de elementos  de la cadena nombresAux
largoPalabra = 0
cantMujeres = 0 #contador de mujeres

valorFecha = '' # variable aux que almacena cada fecha de la lista fechas
aux = []


aH = 2023 #año actual
mH = 5 #mes actual
dH = 17 #dia actual

promedioEdad = 0


print('Iniciales y apellidos de las personas es: ')
for i in range(len(nombres)):
    nombresAux = nombres[i]
    posicionNombre = nombresAux.find(',')
    print(nombresAux[posicionNombre + 2],'. ',nombresAux[0:posicionNombre])

for i in range(len(nombres)):
    nombresAux = nombres[i]
    posicionNombre = nombresAux.find(',')
    contador = 0
    for j in range(posicionNombre, len(nombresAux)):
        contador = contador + 1

    if contador > largoPalabra:
        nombreMasLargo = nombresAux[posicionNombre + 1 :len(nombresAux)]
        largoPalabra = contador

print('El nombre mas largo es: ', nombreMasLargo)

valorCadenaFecha = 0
for i in range(len(fechas)):
    if sexos[i] == 'f':
        cantMujeres = cantMujeres + 1
        valorFecha = fechas[i]
        aux = valorFecha.split('/')
        for j in range(len(aux)):
            if j == 2:
                aN = int(aux[j])
            elif j == 1:
                mN = int(aux[valorCadenaFecha + 1])
            elif j == 0:
                dN = int(aux[valorCadenaFecha])
        edad = aH - aN
        if (mN > mH) or ((mN == mH) and (dN > dH)):
            edad -= 1

        promedioEdad = promedioEdad + edad

promedioEdad = promedioEdad / cantMujeres
print('El promedio de edad de las mujeres es: ', int(promedioEdad))



    

