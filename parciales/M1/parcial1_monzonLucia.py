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

#Quiero obtener:

# 1) La cantidad de clientes de La Carlota.

print("1)")

contador = 0

for lugar in datos:
    recorteElementos = lugar.split("#")
    recorteLugar = recorteElementos[3]
    if recorteLugar == "La Carlota":
        contador+=1
print("La cantidad de clientes de la carlota es",contador)


# 2) El total de deuda acumulada de los clientes que deben más de 90 mil pesos.

print("2)")

total = 0

for deuda in datos:
    recorteElementos = deuda.split("#")
    recorteDeuda = int(recorteElementos[2])
    if recorteDeuda > (90_000):
       deuda = recorteDeuda
       total += deuda
print("El total de deuda acumulada de los grandes deudores es de $",total)
  
   
# 3) Los apellidos de los clientes cuyos DNI sean mayores a 40 millones son:
#    Raynard
#    Dominetti
#    Aronsohn
#    Farrell
#    Dumingo
#    Mingauld


print("3)")

mayores = []
cadena = ""

for apellidos in datos:
    recorteElementos = apellidos.split("#")
    recorteClientes = recorteElementos[1]
    dni = int(recorteElementos[0])
    recorteApellidos = recorteClientes.split(" ")
    apellido = recorteApellidos[1]
    
    if dni > (40_000_000):
        mayores.append(apellido)

for i in range(len(mayores)):
    cadena = cadena+mayores[i]+" \n"

print("Los apellidos de los clientes cuyos DNI sean mayores a 40 millones son:")
print(cadena)




