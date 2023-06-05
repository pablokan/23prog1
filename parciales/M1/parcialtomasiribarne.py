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
ccarlota = 0
for clientes in datos:
    dni, nombre, deuda, localidad = clientes. split('#')
    if localidad == "La Carlota":
     ccarlota = ccarlota + 1 
    
print("La cantidad de clientes de La Carlota", ccarlota)


deudamaX = 0 
for clientes in datos:
    dni, nombre, deuda, localidad = clientes. split('#')
    deuda = int(deuda)
    if deuda <= 0:
        dmax90 = dmax90 + 1 
print("el total de deuda acumulada es:", deuda)

apellido = 0
for x in range (len(datos)):
   reemplazar = datos [x].split('#')
   buscar = reemplazar [1]
   espacio = buscar.split (" ")   
   apellido = espacio [1]   
   dni = int (reemplazar[0])
   if dni > 40000000:
      print(apellido)
      