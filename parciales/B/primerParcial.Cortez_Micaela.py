datos = [
'37572991#Shauna Romanov#137345#Villa María',
'43666785#Brenden Raynard#48176#Villa María',
'33950484#Ronna Massingham#187725#Villa María',
'31735292#Mirabella Fitzpayn#111838#Sampacho',
'44444776#Amabelle Dominetti#39495#Villa María',
'42872667#Grady Aronsohn#34119#La Carlota',
'36482697#Kalinda Lamplough#134823#Sampacho',
'39917430#Clemmy Grigorian#37985#Sampacho',
'47692622#Arley Farrell#105085#Río Cuarto',#16
'20765699#Elmore Godber#130063#La Carlota',
'43509224#Tessa Dumingo#94858#Villa María',
'22334742#Wheeler Tetford#53174#La Carlota',
'35595922#Eachelle Ronaghan#157894#Río Cuarto',#17
'30420756#Drucy Corriea#109433#La Carlota',
'35296538#Beatrisa Wanden#157237#Río Cuarto',#17
'38077386#Debi Shine#38621#Río Cuarto',#16
'36431955#Timothea Simonson#165769#Río Cuarto',#17
'34528663#Chrissy Sainsbury#104154#Sampacho',
'43839759#Leonid Mingauld#106125#Sampacho',
'19987470#Rasla Frankiewicz#139459#Villa María'
]
#1-obtener el apellido del mayor deudor es: Massingham
#2-El total de deuda acumulada de los riocuartenses es de $624606
#3-Los nombres de pila de los clientes cuyos DNI comiencen con 2 son:
#Elmore
#Wheeler
apellido= ""
nombrePila=""
Dni=""
deudaTotal=""
primerNumeroDni=""

for dato in datos:
   espacio= dato.find(" ")
   segundoNumeral= dato.find("#")
   apellido= dato[espacio:segundoNumeral]
   PrimerNumeral= dato.find("#")
   nombre= dato[PrimerNumeral+1:espacio]
   Dni= dato[0:PrimerNumeral]
   #tercerNumeral= dato.find()
   finLocalidad= dato.find("'")
   rioCuarto=dato[-10:]
   primerNumeroDni= dato[0:1]
   deudaRC= dato[-17:-11]
   
   #print(nombre)
   #print(Dni)
   #print(primerNumeroDni)
   
      
   if primerNumeroDni=="2":
      if Dni>primerNumeroDni:
         primerNumeroDni=Dni
         nombrePila += ", "  + nombre
print("los ducumentos de las personas que comienzan en 2 son: "+nombrePila)  


   
      





