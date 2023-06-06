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
# Buscar el mail de cualquier inversor por nombre y mostrarlo.
eleccion = input("Ingrese un numero del 1 al 3: ")
if eleccion == ('1'):
    nombreI = input('Ingrese el nombre a buscar: ')
    nombres = []
    mail = []

    for persona in inversores:
        datos = persona.split(',')
        n = datos[1]
        nombres.append(n)
        gmail = datos[2]
        mail.append(gmail)

    for x in range(len(nombres)):
        if nombreI.lower() == nombres[x].lower():
            print('Nombre:', nombres[x], '    ','Mail:', mail[x])

# Obtener el total de todas las inversiones realizadas en el año 2021
elif eleccion == ('2'):
    año2021 = []
    cont = 0

    for inversion in inversiones:
        datos = inversion.split('-')
        fecha = datos[1]
        fecha1 = fecha.split('/')
        año = fecha1[2]

        if año == '2021':
            año2021.append(inversion)
            monto = datos[0].split(':')
            m = monto[1]
            monto1 = m.split('$')
            m1 = monto1[1]
            cont += float(m1)

    print("Inversiones en 2021:")
    for inversion in año2021:
        print(inversion)

    print("El total de inversiones en 2021 fue de:", cont)

    
# Saber cuantas inversiones fueron realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino.
elif eleccion == ('3'):
    fechas = []
    invmujeres = []
    cont = 0

    for inversor in inversores: 
        datos = inversor.split(',')
        f = datos[1]
        if datos[3] == "Female":
            invmujeres.append(inversor)

    for inversion in inversiones:
        fecha = inversion.split('-')
        fecha1 = fecha[1]
        fecha2 = fecha1.split('/')
        año = int(fecha2[2])
        mes = int(fecha2[1])
        if año == 2022 and mes <= 6:
            fechas.append(fecha1)
    print("Cantidad de inversiones realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino:", len(fechas))
    #Este ultimo me da el resultado de todas las mujeres, pero no respeta la consigna de durante el primer trimestre. No llegue a corregirlo.
    


        
