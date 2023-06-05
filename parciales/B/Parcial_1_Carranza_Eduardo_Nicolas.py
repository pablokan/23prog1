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
#   Listas
lista_dni = []
lista_nombre = []
lista_deuda = []
lista_lugar = []
lista_apellido = []
lista_deuda_entero = []
lista_nombre_solo = []
lista_primer_nro = []
lista_nombre_ej3 = []
#   Contadores
c = -1
c2 = -1
c3 = -1
c4 = -1
c5 = -1
c6 = -1
c7 = -1
c8 = -1
#   Listas Completas
for i1 in range(len(datos)):
    c = c + 1
    datos_separo = datos[c].split("#")
    dni = datos_separo[0]
    lista_dni.append(dni)
#   ----------------------------------
for i2 in range(len(datos)):
    c2 = c2 + 1
    datos_separo = datos[c2].split("#")
    nombre = datos_separo[1]
    lista_nombre.append(nombre)
    subnombre = nombre.split(" ")
    apellido = subnombre[1]
    lista_apellido.append(apellido)
    nombre_solo = subnombre[0]
    lista_nombre_solo.append(nombre_solo)
#   -----------------------------------
for i3 in range(len(datos)):
    c3 = c3 + 1
    datos_separo = datos[c3].split("#")
    deuda = datos_separo[2]
    #convertir en entero

    lista_deuda.append(deuda)
    lista_deuda_entero.append(int(lista_deuda[c3]))
#   -----------------------------------
for i4 in range(len(datos)):
    c4 = c4 + 1
    datos_separo = datos[c4].split("#")
    lugar = datos_separo[3]
    lista_lugar.append(lugar)
#   ------------------------------------


#   ------------- Consigna 1 ---------------------
cantidad_deuda = 0

for e1 in range(len(datos)):
    c5 = c5 +1
    if lista_deuda_entero[c5] > cantidad_deuda :
        cantidad_deuda = lista_deuda_entero[c5]
        mostrar_apellido = lista_apellido[c5]
print("El apellido del mayor deudor es:", mostrar_apellido)


#   ------------- Consigna 2 ---------------------

suma_deuda = 0
suma_deuda2 = 0
for e2 in range(len(datos)):
    c6 = c6 + 1
    if lista_lugar[c6] == "Río Cuarto":
        sub_suma = lista_deuda_entero[c6]
        suma_deuda = sub_suma + suma_deuda
print("El total de deuda acumulada de los riocuartenses es de:  ",suma_deuda)

#   ------------- Consigna 3 ----------------------

for e3 in range(len(datos)):
    c7 = c7 + 1
    dni2 = lista_dni[c7]
    primer_nro = dni2[0]
    lista_primer_nro.append(primer_nro)
    if lista_primer_nro[c7] == "2":
        sub_nombre2 = lista_nombre[c7]
        nombre_solo2 = sub_nombre2.split(" ")
        nombre_solo3 = nombre_solo2[0]
        lista_nombre_ej3.append(nombre_solo3)
print("Los nombres de pila de los clientes cuyos DNI comiencen con 2 son: ")
for e4 in range(len(lista_nombre_ej3)):
    print(lista_nombre_ej3[e4])
