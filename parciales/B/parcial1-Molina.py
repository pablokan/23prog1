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
#1)El apellido del mayor deudor es: Massingham 
#2)El total de deuda acumulada de los riocuartenses es de $624606
#3)Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:Elmore-Wheeler
deudores=""
mayordeudor=0
print("1)")
for i in range (len(datos)):
    c=datos[i]
    p=c.split("#")
    for v in range (len(p)):
        if v==1:
            n=p[v]
        elif v==2:
            cantidad = int(p[v])
            if mayordeudor<cantidad:
                mayordeudor=cantidad
                deudores=n
e=deudores.find(" ")
apellido=deudores[e + 1:]
print("El más deudor es:",apellido)

print("2)")
deudarioiv=[]
total=0
for i in range(len(datos)):
    c=datos[i]
    p=c.split("#")
    for v in range (len(p)):
        if v==2:
            cantidad=int(p[v])
        elif v==3:
            ciudad=(p[v])
            if ciudad=="Río cuarto":
                total=total+cantidad
print("El total de la deuda es:",total)