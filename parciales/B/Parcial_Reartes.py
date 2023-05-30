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
personas = []
nombres = []
deudas = []
dni = []
localidades = []
for element in datos:
    persona = element.split("#")
    personas.append(persona)
    #print(split)
#print(personas)
for i in range(len(personas)):
    dni.append(personas[i][0])
    nombres.append(personas[i][1])
    deudas.append(int(personas[i][2]))
    localidades.append(personas[i][3])
#print(nombres)
#print(deudas)
#print(dni)
#print(localidades)

max = 0
deudor = " "
nombresPila = []
apellidos = []
for element in nombres:
    apellido = element.split(" ")
    nombresPila.append(apellido[0])
    apellidos.append(apellido[1])
    
#print(apellidos)
#print(nombresPila)
for i in range(len(deudas)):
    if deudas[i] > max:
        deudor = apellidos[i]
        max = deudas[i]
print("El apellido del mayor deudor es:",deudor)
total = 0
for i in range(len(localidades)):
    if localidades[i] == "Río Cuarto":
        total = total + deudas[i]
print("El total de la deuda de los riocuartenses es de: $",total)
print("Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:")
for i in range(len(dni)):
     if dni[i][0] == "2":
        print(nombresPila[i])