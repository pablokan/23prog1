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

#La cantidad de clientes de La Carlota.
#salida esperada: la cantidad de La Carlota seria: 4

clientes_carlota = 0

for clientes in datos:
    dni, nombre ,deuda, localidad = clientes. split("#")
    if localidad == "La Carlota":
        clientes_carlota = clientes_carlota + 1
        
        print("La cantidad de clientes de La Carlota seria:",clientes_carlota)

       # El total de deuda acumulada de los clientes que deben más de 90 mil pesos.
       #salida esperada: El total de deuda acumulada de las grandes deudas es de $1841808

debe_maxima_90 = 0

for clientes in datos:
    dni, nombre, debe, localidad = clientes. split("#")
    debe = int(debe)
    if debe >= 90000:
            debe_maxima_90 = debe_maxima_90 + debe
            print("el tota de la deuda acumulada de los grandes deudores es de:", debe_maxima_90)

#Los apellidos de los clientes cuyos DNI sean mayores a 40 millones.
#salida esperada:
""" Los apellidos de los clientes cuyos DNI sean mayores a 40 millones son:
Raynard
Dominetti
Aronsohn
Farrell
Dumingo
Mingauld
"""

apellido = []
for clientes in datos:
    dni, nombre, deuda, localidad = clientes. split("#")
    dni = int(dni)
    if dni >= 40000000: 
     apellido.append(nombre.split()[1])

     print("los apellidos de los clientes segun sus dni sean mayores a 40 millones son:")
     for i in range(len(apellido)):
            print(apellido[i])






        


        





