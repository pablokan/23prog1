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
nombres=[]
apellidos=[]
deudas=[]
dnis=[]
ciudades=[]
for persona in datos:
    listaPersona=persona.split("#")
    dnis.append(listaPersona[0])
    nombreYapellido=listaPersona[1]
    nombres.append(nombreYapellido.split(" ")[0])
    apellidos.append(nombreYapellido.split(" ")[1])
    deudas.append(listaPersona[2])
    ciudades.append(listaPersona[3])

mayorDeuda=0
deudaTotal=0
indice=0
for deuda in deudas:
    deuda=int(deuda)
    if ciudades[indice]=="Río Cuarto":
        deudaTotal+=deuda
    if deuda>mayorDeuda:
        mayorDeuda=deuda
        mayor=indice
    indice+=1

print ("El apellido del mayor deudor es: ",apellidos[mayor])
print("El total de deuda acumulada de los riocuartenses es de $"+str(deudaTotal))
indice=0
print("Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:")
for nombre in nombres:
    if dnis[indice][0]=="2":
        print(nombres[indice])
    indice+=1