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
print("1)")
contador=0
for cliente in datos:
    clientes=cliente.split('#')
    localidad=clientes[3]
    if localidad == "La Carlota":
        contador+=1
print("La cantidad de clientes de La Carlota es",contador)
print("2)")
acum=0
for cliente in datos:
    clientes=cliente.split("#")
    deuda=int(clientes[2])
    if deuda>90000:
        acum+=deuda
print("El total de deuda acumulada de los grandes deudores es de $",acum)
print("3)")
for cliente in datos:
    clientes=cliente.split("#")
    dni=int(clientes[0])
    if dni > 40000000:
        nombre=clientes[1]
        posespacio=nombre.find(" ")
        apellido=nombre[posespacio:]
        print(apellido)