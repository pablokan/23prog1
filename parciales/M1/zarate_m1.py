# Quiero obtener:
# La cantidad de clientes de La Carlota.
# El total de deuda acumulada de los clientes que deben más de 90 mil pesos.
# Los apellidos de los clientes cuyos DNI sean mayores a 40 millones.



# La cantidad de clientes de La Carlota.

clientesLacarlota = [

'42872667#Grady Aronsohn#34119#La Carlota',
'20765699#Elmore Godber#130063#La Carlota',
'22334742#Wheeler Tetford#53174#La Carlota',
'30420756#Drucy Corriea#109433#La Carlota',
]

cantidad_clientes = len(clientesLacarlota)
print("1) La cantidad de clientes es:", cantidad_clientes)

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
# El total de deuda acumulada de los clientes que deben más de 90 mil pesos.

clientes = [
    {"Shauna Romanov": "Cliente1", "deuda": 137345 },
    {"Ronna Massingham": "Cliente2", "deuda": 187725},
    {"Mirabella Fitzpayn": "Cliente3", "deuda": 111838},
    {"Kalinda Lamplough": "Cliente4", "deuda": 134823},
    {"Elmore Godber": "Cliente5", "deuda": 130063 },
    {"Tessa Dumingo": "Cliente6", "deuda": 94858 },
    {"Drucy Corriea": "Cliente7", "deuda": 109433 },
    {"Eachelle Ronaghan": "Cliente7", "deuda": 157894 },
    {"Beatrisa Wanden": "Cliente7", "deuda": 157237 },
    {"Timothea Simonson": "Cliente7", "deuda": 165769 },
    {"Chrissy Sainsbury": "Cliente7", "deuda": 104154 },
    {"Leonid Mingauld": "Cliente7", "deuda": 106125 },
    {"Rasla Frankiewicz": "Cliente7", "deuda": 139459 },
]
total_deuda_acumulada = 0

for cliente in clientes:
    if cliente["deuda"] > 90000:
        total_deuda_acumulada += cliente["deuda"]

print("2) El total de deuda acumulada de los clientes que deben más de 90 mil pesos es:", total_deuda_acumulada)

# buscar los apellidos de los clientes cuyos DNI sean mayores a 40 millones.

clientes = [
    {"dni": 43666785, "apellido":"Raynard"},
    {"dni": 44444776, "apellido":"Dominetti"},
    {"dni": 42872667, "apellido":"Aronsohn"},
    {"dni": 47692622, "apellido":"Farrell"},
    {"dni": 43509224, "apellido":"Dumingo"},
    {"dni": 43839759, "apellido":"Mingauld"},
]

apellidos_mayor_40m = []
for cliente in clientes:
    if cliente["dni"] > 40000000:
        apellidos_mayor_40m.append(cliente["apellido"])
print(apellidos_mayor_40m)

