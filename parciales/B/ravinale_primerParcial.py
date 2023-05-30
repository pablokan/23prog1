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

#Ejercicio 1


personamasdeudora=""
masdeudor=0
for i in range (len(datos)):
    cadena = datos[i]
    personas = cadena.split("#")
    for dp in range (len(personas)):
        if dp == 1:
            nombre=personas[dp]
        elif dp == 2:
            monto = int(personas[dp])
            if masdeudor < monto:
                masdeudor = monto
                personamasdeudora = nombre
espacio= personamasdeudora.find(" ")
apellido = personamasdeudora[espacio + 1:]
print ("La persona mas deudora es", apellido, "con un monto de: ", masdeudor)

#Ejercicio 2


deudoresRioCuarto=[]
montoTotal=0
for i in range (len(datos)):
    cadena = datos[i]
    personas = cadena.split("#")
    for dp in range (len(personas)):
        if dp == 2:
            monto=int(personas[dp])
        elif dp == 3:
            ciudad = (personas[dp])
            if  ciudad == "Río Cuarto":
                montoTotal= montoTotal + monto

print ("El monto total de la deuda de las personas de Rio Cuarto es: $", montoTotal)

#Ejercicio 3
        

dni=""
nombre=[]
for i in range (len(datos)):
    cadena = datos[i]
    personas = cadena.split("#")
    for dp in range (len(personas)):
        if dp == 0:
            dni = int(personas[dp])
            if dni < 30000000 and dni > 19999999:
                nombreCompleto=personas[1]
                espacio= nombreCompleto.find(" ")
                nombreSolo=nombreCompleto[:espacio]
                nombre.append(nombreSolo)
        
print ("La personas deudoras con un DNI que comience en 2 son: ", nombre)



    
    





