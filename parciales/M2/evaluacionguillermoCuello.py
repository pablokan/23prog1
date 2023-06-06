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
    '12,Fionna,fshanksterb@mashable.com,Female,Ccuntuma',
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
    'Monto: $136930.77 - Fecha:07/08/2022',
    'Monto: $925498.10 - Fecha:16/08/2021',
    'Monto: $634854.83 - Fecha:22/05/2022',
    'Monto: $682885.94 - Fecha:26/04/2022',
    'Monto: $748880.01 - Fecha:02/09/2022',
    'Monto: $490253.97 - Fecha:26/02/2022',
    'Monto: $953863.00 - Fecha:29/01/2022',
    'Monto: $473316.46 - Fecha:21/07/2022',
    'Monto: $193841.90 - Fecha:21/11/2021',
    'Monto: $325836.11 - Fecha:20/06/2022',
    'Monto: $632385.67 - Fecha:17/07/2022',
    'Monto: $137358.07 - Fecha:30/11/2021',
    'Monto: $320210.52 - Fecha:20/05/2022',
    'Monto: $558827.34 - Fecha:10/05/2022',
    'Monto: $140948.04 - Fecha:25/06/2022'
]

#1)Buscar el mail de cualquier inversor por nombre y mostrarlo
nombreAB = input ('ingresar nombre a buscar: ')
nombresL = []
gmailsL = []
for persona in inversores :
    datos = persona.split(",")
    nombres = datos[1]
    nombresL.append(nombres)
    gmails = datos[2]
    gmailsL.append(gmails)
for i in range (len(nombresL)):
    if nombreAB == nombresL[i]:
     print ("el gmail de ",nombresL[i],"es: ",gmailsL[i])




#2)Obtener el total de todas las inversiones realizadas en el año 2021
""" total = 0
S21 = []

f2021 = []
for dato in inversiones:
    datos1 = dato.split("-")
    montos = datos1[0].split(":")
    sinsigno = montos[1].split('$')
    fechas = datos1[1].split(":")
    fechasS = fechas[1].split('/')
    if fechasS[2] == "2021":
        f2021.append(fechasS)
        S21.append(sinsigno[1])

for limpio in S21:
    solN = float(limpio)  
    total = total + solN

print('el total de las inversiones es:$',round(total)) """

#3)Saber cuantas inversiones fueron realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino.
""" fechasS = []
SexosM = []

for persona in inversores :
    datos = persona.split(',')
    sexos = datos[3]
    SexosM.append(sexos)
    nombres = datos[1]

    for dato in inversiones :
        datos2 = dato.split('-')
        montos = datos2[0].split(":")
        sinsigno = montos[1].split('$')
        fechas = datos2[1].split(':')
        fechass =fechas[1].split('/')
        if int(fechass[1]) < 6 and sexos == 'Female' :
            fechasS.append(fechass)
            fechasS.append(nombres)
            fechasS.append(sinsigno)


print (fechasS) """#el problema esta soluciado pero me muestra en repetidas ocasiones lo mismo
            














