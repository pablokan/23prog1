inversores = [
    "1,Veriee,vvasilkov0@qq.com,Female,Besançon",
    "2,Lizbeth,locklin1@tiny.cc,Female,Jawand",
    "3,Tymon,thillum2@diigo.com,Male,Rîbniţa",
    "4,Teddie,tschofield3@ehow.com,Male,Tlogoagung",
    "5,Dom,dantonin4@squarespace.com,Male,Tonjongsari",
    "6,Armstrong,acreegan5@reverbnation.com,Male,Xianning",
    "7,Micky,mmaccall6@elpais.com,Female,Dongping",
    "8,Mickie,mprosser7@alexa.com,Male,Perm",
    "9,Nadya,ngerrett8@over-blog.com,Female,Champaign",
    '10,Donni,dboots9@digg.com,Female,Normanton',
    "11,Dalli,dmorecombea@wordpress.com,Male,Serra",
    '12,Fiodor,fshanksterb@mashable.com,Male,Ccuntuma',
    "13,Melesa,mmacinnesc@si.edu,Female,Shihua",
    '14,Orelle,oshobbrookd@t.co,Female,Huangtan',
    '15,Gayelord,ghasloche@gmpg.org,Male,Sehwān',
    '16,Florencia,fforstf@addthis.com,Female,Buenavista',
    '17,Pam,pbelfeltg@lulu.com,Female,Maclear',
    '18,Ollie,okubalekh@feedburner.com,Female,Kebon',
    '19,Wyn,wlingeri@dropbox.com,Male,Gimry',
    '20,Vachel,vburbankj@topsy.com,Male,Bungoma'
    ]

inversiones = [
    'Monto: $374324.12 - Fecha:09/04/2022',
    'Monto: $423222.26 - Fecha:14/09/2021',
    'Monto: $591323.65 - Fecha:08/01/2022',
    'Monto: $279894.15 - Fecha:12/05/2022',
    'Monto: $884488.11 - Fecha:04/03/2022',
    'Monto: $136930.77 - Fecha:07/08/2021',
    'Monto: $925498.10 - Fecha:16/08/2021',
    'Monto: $634854.83 - Fecha:22/05/2022',
    'Monto: $682885.94 - Fecha:26/04/2022',
    'Monto: $748880.01 - Fecha:02/09/2022',
    'Monto: $490253.97 - Fecha:26/02/2022',
    'Monto: $953863.00 - Fecha:29/11/2021',
    'Monto: $473316.46 - Fecha:21/07/2022',
    'Monto: $193841.90 - Fecha:21/11/2021',
    'Monto: $325836.11 - Fecha:20/06/2022',
    'Monto: $632385.67 - Fecha:17/07/2022',
    'Monto: $137358.07 - Fecha:30/11/2021',
    'Monto: $320210.52 - Fecha:20/05/2022',
    'Monto: $558827.34 - Fecha:10/05/2022',
    'Monto: $140948.04 - Fecha:25/06/2022'
]

""" Quiero hacer lo siguiente:

-Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)
-Decir el monto de la mayor inversión realizada en el 2022.
-Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021 por 
inversores de sexo masculino.


Salidas esperadas:
-El nombre de la persona que vive en Dongping es: Micky
-La mayor inversión del año 2022 fue de: $884488.11
-El total de fondos invertidos por varones en el segundo semestre del 2021 fue de $1090793.77 """


nombreCiudad = input('Ingrese nombre de una ciudad, para luego encontrar su respectivo inversor: ')
listaPorPersona = []
noHayInversorCiudad = False
for elementosInversores in inversores: #Recorremos toda la lista por cada elemento que la compone.
    listaPorPersona = elementosInversores.split(',') #Hacemos una subcadena llamada listaPorPersona, dentro de ella obtenemos 5 nuevos elementos par obtener el nombre de la ciudad y nombre d ela persona.
    if listaPorPersona[4] == nombreCiudad: # ListaPorPersona[4] es el elemento de la subcadena que contiene el nombre de la ciudad
        print('El nombre de la persona que vive en',listaPorPersona[4],'es:', listaPorPersona[1])
        noHayInversorCiudad = True #verifica que halla personas en la busqueda.
if noHayInversorCiudad == False:#verifica que halla personas en la busqueda.
    print('No hay inversores en esta ciudad.')

fechaBuscada = 2022
mayorInvercion = 0 #variable donde asignaremos la mayor invercion.
for elementoInversiones in inversiones:#Recorremos toda la lista por cada elemento que la compone.
    fechaElemento = int(elementoInversiones[-4:]) #extraemos por slicing el año de cada elemento y se lo asignamos a la variable fechaElemento
    montoElemento = float((elementoInversiones.split(' - ')[0]).split('$')[1])#Hacemos un split para obtener dos subcadenas, y tomamos el elemento 1 para asignarlo a la variable montoElemento. Con esto extraemos los montos invertidos.
    if mayorInvercion < montoElemento and fechaElemento == fechaBuscada:
        mayorInvercion = montoElemento
print('La mayor inversión del año',fechaBuscada,'fue de:', '$'+str(round(mayorInvercion,2)))

fechaBuscada2 = 2021
listaPorPersona = []
totalInverciones = 0
for i in range(len(inversores)):
    listaPorPersona = inversores[i].split(',')
    aFecha = int(inversiones[i][-4:]) #extraemos por slicing el año de cada elemento y se lo asignamos a aFecha
    mFecha = int(inversiones[i][-7:-5])  #extraemos por slicing el mes de cada elemento y se lo asignamos a mFecha
    montoElemento = float((inversiones[i].split(' - ')[0]).split('$')[1])#Hacemos un split para obtener dos subcadenas, y tomamos el elemento 1 para asignarlo a la variable montoElemento. Con esto extraemos los montos invertidos.
    if listaPorPersona[3] == 'Male' and aFecha == fechaBuscada2 and 6<mFecha<13: 
        totalInverciones += montoElemento #acumulador donde sumaremos los montos de las inverciones buscadas.
print('El total de fondos invertidos por varones en el segundo semestre del',fechaBuscada2,'fue de: ', totalInverciones) 