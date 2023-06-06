""" Tengo dos listas paralelas de clientes de Fondos de Inversión. 
La primera lista tiene un número de cliente, su nombre, mail, sexo y ciudad.
La segunda lista tiene el monto de la inversión y la fecha de la misma.
 """
# 1) Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)
# 2) Decir el monto de la mayor inversión realizada en el 2022.
# 3) Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021 por inversores de sexo masculino.




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


ciudad = []
nombres = []
sexos = []

for inversor in inversores:
    ciudad.append(inversor.split(",")[4])
    nombres.append(inversor.split(",")[1])
    sexos.append(inversor.split(",")[3])
# print(ciudad)
# print(nombre)

ciudadBuscar = "Dongping"

for i in range(len(ciudad)):
    if ciudad[i] == ciudadBuscar:
        print("La persona de " + ciudadBuscar + " se llama " + nombres[i])

años = []
meses = []
montos = []

for date in inversiones:
    años.append(date[-4:])
    meses.append(int(date[-7:-5]))
    montos.append(date.split(" ")[1])

montosInt = []
centavosMontos = []
for monto in montos:
    montoEntero = (monto.split("$")[1])
    
    # print(montoEntero)
    comaAux = montoEntero.find(".")
    montosInt.append(int(montoEntero[:comaAux]))
    centavosMontos.append(int(montoEntero[comaAux + 1:]))

anoBuscar = "2022"
montoComparador = 0
montoMax = ""

for x in range(len(años)):
    if años[x] == anoBuscar:
        if montosInt[x] > montoComparador:
            montoComparador = montosInt[x]
            montoMax = montos[x]

print("La mayor inversion del ano " + anoBuscar + " fue de: " + montoMax)

sexoBuscar = "Male"
añoBuscar = "2021"
mesBuscar = 6
contadorCentavos = 0
contadorInversiones = 0
for z in range(len(sexos)):
    if sexos[z] == sexoBuscar:
        if añoBuscar == años[z] and meses[z] >= mesBuscar:
            contadorInversiones = contadorInversiones + montosInt[z] 
            contadorCentavos = contadorCentavos + centavosMontos[z]

print("El total de fondos invertidos por varones en el segundo semestre del 2021 fue de $" + str(contadorInversiones) + "." + str(contadorCentavos))


# print(montos)
# print(fechas)
