#Quiero obtener:
#La cantidad de clientes de La Carlota.
#El total de deuda acumulada de los clientes que deben más de 90 mil pesos.
#Los apellidos de los clientes cuyos DNI sean mayores a 40 millones.


datos = [
'37572991#Shauna Romanov#137345#Villa María',
'43666785#Brenden Raynard#48176#Villa María',
'33950484#Ronna Massingham#187725#Villa María',
'31735292#Mirabella Fitzpayn#111838#Sampacho',
'44444776#Amabelle Dominetti#39495#Villa María',
'42872667#Grady Aronsohn#34119#La Carlota',
'36482697#Kalinda Lamplough#134823#Sampacho',
'39917430#Clemmy Grigorian#37985#Sampacho',
'47692622#Arley Farrell#105085#Río Cuarto',
'20765699#Elmore Godber#130063#La Carlota',
'43509224#Tessa Dumingo#94858#Villa María',
'22334742#Wheeler Tetford#53174#La Carlota',
'35595922#Eachelle Ronaghan#157894#Río Cuarto',
'30420756#Drucy Corriea#109433#La Carlota',
'35296538#Beatrisa Wanden#157237#Río Cuarto',
'38077386#Debi Shine#38621#Río Cuarto',
'36431955#Timothea Simonson#165769#Río Cuarto',
'34528663#Chrissy Sainsbury#104154#Sampacho',
'43839759#Leonid Mingauld#106125#Sampacho',
'19987470#Rasla Frankiewicz#139459#Villa María'
]

#Primer proceso, contar las personas que hay en una zona (en este caso, en La Carlota)
#La salida esperada es: "La cantidad de clientes de La Carlota es 4"
#El input seria: La Carlota
lugarAnalizar = input("Ingrese la zona en la cual quiere saber cuantas personas hay: ")

localidades = []
for persona in datos:
    listaDatos = persona.split("#")
    localidad = listaDatos[3]
    localidades.append(localidad)

contador = 0
for lugar in localidades:
    if lugarAnalizar == lugar:
        contador = contador + 1

print("1)" ,'La cantidad de clientes de',lugarAnalizar, 'es', contador)
#Primer proceso listo

#Segundo proceso, obtener el total de la deuda de los clientes que deban mas de 90 mil pesos
#La salida esperada es: "El total de deuda acumulada de los grandes deudores es de $1841808"

deudas = []    #esta lista va a contener los enteros, no las strings de las deudas

for elemento in datos:
    listaDatos = elemento.split("#")
    deudaCliente = listaDatos[2]
    deudas.append(int(deudaCliente))

acumulador = 0
for dinero in deudas:
    if dinero > 90000:
        acumulador = acumulador + dinero

print("2)" ,'El total de la deuda acumulada de los grandes deudores es de', '$' ,acumulador)
#Segundo proceso listo

#Tercer proceso, obtener los apellidos de aquellas personas cuyo numero de documento sea mayor a 40 millones
#La salida esperada es: "Los apellidos de los clientes cuyos DNI sean mayores a 40 millones son:
                                                                                        #Raynard
                                                                                        #Dominetti
                                                                                        #Aronsohn
                                                                                        #Farrell
                                                                                        #Dumingo
                                                                                        #Mingauld



apellidos = []     #con esta lista guardo los apellidos de las personas
documentos = []     #con esta lista guardo los documentos para comparar los mayores a 40 millones
for elem in datos:
    listaDatos = elem.split("#")
    doc = int(listaDatos[0])
    if doc > 40000000:
        nombreCompleto = listaDatos[1]
        nombreYapellido = nombreCompleto.split()
        apellido = nombreYapellido[1]
        apellidos.append(apellido)

print("3)" ,"Los apellidos de los clientes cuyos DNI sean mayores a 40 millones son:")
for apel in apellidos:
    print(apel)
