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

# 1) Conseguir el nombre del mayor deudor

list = []
deudor = ''
deudamax = 0
for element in datos:
    list = element.split('#')
    deuda = int(list[2])
    if deuda > deudamax:
        deudamax = deuda
        deudor = list[1]
deudor = deudor.split(' ')
deudor = deudor[1]

# Salida esperada: El apellido del mayor deudor es: Massingham 

print('El apellido del mayor deudor es:', deudor)

# 2) Declarar la deuda acumulada de todos los riocuarteces
localidad = input('Ciudad a buscar. Recuerde poner bien los acentos y mayusculas: ')
ciudad = ''
deudatotal = 0
for element in datos:
    list = element.split('#')
    ciudad = list[3]
    deuda = int(list[2])
    if ciudad == localidad:
        deudatotal = deudatotal + deuda

# Salida esperada: El total de deuda acumulada de los riocuartenses es de $624606

print('El total de deuda acumulada de los riocuartenses es de', deudatotal)

# 3) Los nombres de todos aquellos que su dni comiencen con 2
num = input('Primer digito del dni: ')
list = []
nombre = []
nombres = []
dni = ''
for element in datos:
    list = element.split('#')
    nombre = list[1].split(' ')
    nombre = nombre[0]
    dni = list[0]
    if dni[0] == num:
        nombres.append(nombre)
# SalidA esperada: Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:
# Elmore
# Wheeler

print('Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:')
for element in nombres:
   print(element)