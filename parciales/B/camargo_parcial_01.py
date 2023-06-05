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

dnis = []
nombresCompletos = []
nombres = []
apellidos = []
deudas = []
ciudades = []

for dato in datos:
    dni = dato.split("#")[0]
    dnis.append (dni)
    nombreCompleto = dato.split("#")[1]
    pos = nombreCompleto.find(" ")
    nombre = nombreCompleto[0:pos]
    nombres.append(nombre)
    apellido = nombreCompleto[pos+1:]
    apellidos.append(apellido) 
    deuda = int(dato.split("#")[2])
    deudas.append(deuda) 
    ciudad = dato.split("#")[3]
    ciudades.append(ciudad) 

#Calculo de deuda

deudaInicial = 0

for deuda in deudas:
    if deuda > deudaInicial:
        deudaInicial = deuda

#1) El apellido del mayor deudor es: Massingham

for x in range (len(deudas)):
    if deudaInicial == deudas[x]:
        print ('1) El apellido del mayor deudor es: ', apellidos[x])

#2) La deuda acumulada de los Río Cuartenses es de: $624606

deudaAcumulada = 0

for x in range (len(ciudades)):
    if ciudades[x] == "Río Cuarto":
        deudaAcumulada += deudas[x]
print ('2) La deuda acumulada de los Río Cuartenses es de: $' + str(deudaAcumulada))

#3) Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:
#Elmore
#Wheeler

print("Los nombres de pila de los clientes cuyos DNI comiencen con 2 son: ")
for x in range (len(dnis)):
    if dnis[x][0] == "2":
        print(nombres[x])        