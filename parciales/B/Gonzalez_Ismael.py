#DNI, nombre y apellido, monto de deuda en pesos y localidad.
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


#El apellido del mayor deudor es: Massingham 

monto_mayor = 0
nombre_masmoroso = ""
for persona in datos:
    dni,nombreYapellido,monto,localidad = persona.split("#")
    nombre = nombreYapellido.split(" ")
    deuda = int(monto)
    if monto_mayor <deuda:
        monto_mayor = deuda
        nombre_masmoroso = nombre[1]
print("el apellido del mayor deudor es:",nombre_masmoroso)

#El total de deuda acumulada de los riocuartenses es de $624606
total_deuda_rc = 0

for persona in datos:
    dni,nombreYapellido,monto,localidad = persona.split("#")
    if "Río Cuarto" == localidad:
        total_deuda_rc += int(monto)
total_deuda_rc = str(total_deuda_rc)
        
print("El total de deuda acumulado de los riocuartenses es de","$"+total_deuda_rc)
    
#DNI empiece con 2 nombre pila elmore y wheeler
print("los nombres de las personas cuyo DNI comienza con (2) son: ")
nombre_pila = ""
for persona in datos:
    dni,nombreYapellido,monto,localidad = persona.split("#")
    nombre = nombreYapellido.split(" ")[0]
    if dni[0] == "2":
        nombre_pila = nombre
        print(nombre_pila)
    
        
   


    
   










