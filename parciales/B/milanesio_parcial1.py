# Tengo una lista con datos de clientes:
# DNI, nombre y apellido, monto de deuda en pesos y localidad.

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

#1 El apellido del mayor deudor es: Massingham 

mayorDeuda = 0
apellidoMayorDeudor = ""

for dato in datos:
    datosCliente = dato.split("#")
    deuda = int(datosCliente[2])
    apellido = datosCliente[1].split()[1]
    if deuda > mayorDeuda:
        mayorDeuda = deuda
        apellidoMayorDeudor = apellido
print("El apellido del mayor deudor es:", apellidoMayorDeudor)


#2 El total de deuda acumulada de los riocuartenses es de $624606

totalDeudaRiocuarto = 0

for dato in datos:
    splitDato = dato.split("#")
    localidad = splitDato[3]
    if localidad == "Río Cuarto":
        montoDeuda = int(splitDato[2])
        totalDeudaRiocuarto += montoDeuda
print(f"El total de deuda acumulada de los riocuartenses es de ${totalDeudaRiocuarto}")


#3 Los nombres de pila de los clientes cuyos DNI comiencen con 2 son: Elmore - Wheeler

nombresPila = []

for dato in datos:
    dni, nombre, montoDeuda, localidad = dato.split("#")
    if dni[0] == "2":
        nombresPila.append(nombre.split()[0])
print("Los nombres de pila de los clientes cuyo DNI comienza con 2 son:")
for nombre in nombresPila:
    print(nombre)

