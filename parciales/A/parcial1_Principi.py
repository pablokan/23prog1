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

#Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)
nombreBuscar = input("Ingrese el nombre que desea buscar: ")
nombresCiudad = []
nombrePersona = []
for nombreInversores in inversores:
    nombresCiudad = nombresCiudad.append(",")
    if nombrePersona == nombresCiudad:
        print("el nombre de la persona que vive en", nombrePersona, "es:", nombresCiudad)


#Decir el monto de la mayor inversión realizada en el 2022.
acumulador = 0
año = 2022
for elementInv in inversiones:
    fechaElemento = int((elementInv.split("-")[1][-4]))
    montoElemento = float((elementInv.split("-")[0]).split("$")[1])
    if fechaElemento == año:
        acumulador += montoElemento
print("La mayor inversión del año 2022 fue de: $", str(round(acumulador,2)))

#Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021 por inversores de sexo masculino.
legajoPersonas = []
año = 2021
contadorInversiones = 0
for i in range(len(inversores)):
    legajoPersonas = inversores[i].split(",")
    aFecha = int(inversiones[i][-4:])
    mFecha = int(inversiones[-7:-5])
    monto = float((inversiones[i].split("-"[0]).split("$")[1]))
    if legajoPersonas[1] == "Male" and aFecha == 2021

print("El total de fondos invertidos por varones en el segundo semestre del", año, "fue de", )
