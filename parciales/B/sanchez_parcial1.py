"""
Salidas esperadas (lo que quiero obtener):

El apellido del mayor deudor es: Massingham 

El total de deuda acumulada de los riocuartenses es de $624606

Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:
Elmore
Wheeler
"""
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

#apellido
#nombres#
#ciudad
#deuda
#dni#
totalDeuda = ""
nombresIniciales = ""
apellidoDeudor = ""

dato = str(datos)
deudaUsuario = ""
#print(listaDividido)
listaDividido = []
listaDni = []
listaNombre = []
listaDeuda = []
listaCiudad = []
for dato in datos:
    listaDividido = dato.split('#')
    listaDni.append(listaDividido[0])
    listaNombre.append(listaDividido[1])
    listaDeuda.append(listaDividido[2])
    listaCiudad.append(listaDividido[3])

    dni = dato[:8]
    
    numeral = dato.find("#")
    espacioUno = dato.find(" ")
    nombre = dato[numeral+1:espacioUno]
    
    
    


#print (dni)
for nombre in listaNombre:
    espacio = nombre.find(" ")
    nombreUsuario = nombre[:espacio]
    apellidoUsuario = nombre[espacio:]

#print(totalDeuda)
#print(deuda)
   # print(nombreUsuario)
  #  print(apellidoUsuario)
#print(apellido)
    #varDividido = str(:)
    #print(varDividido)
    #print(listaDividido)
    
    #print(listaDividido)
 #   print(elemento)
   # dni = dato[:8]
    #print(dni)
    
   # numeral = dato.find("#")
    #espacioUno = dato.find(" ")
    #nombre = dato[numeral+1:espacioUno]
    #print(nombre)
    
   
  #  espacioDividido = varDividido.find(" ")
  #  print(espacioDividido)
    #apellido = espacioDividido[espacioDividido:]
    #print(apellido)

  #  numeralTres = dato.find("#")
   # ciudad = dato[numeralTres:]
    #print(ciudad)

#print(listaDni)
#print(listaNombres)
#for dividido in listaDividido:
 #   print(listaDividido)
