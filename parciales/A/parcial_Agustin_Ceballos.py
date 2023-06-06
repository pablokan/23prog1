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

inversionesFecha = [
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

posicion = []
nombres = []
email = []
sex = []
ciudad = []
monto = []
fecha = []

for inversor in inversores:
    array = inversor.split(",")

    posicion.append(array[0])
    nombres.append(array[1])
    email.append(array[2])
    sex.append(array[3])
    ciudad.append(array[4])

city = input("Ingrese ciudad a buscar: ")
for pos in range(len(posicion)):
    if ciudad[pos] == city:
        print("La persona que vive en",ciudad[pos],"es:",nombres[pos])

for montoInversor in inversionesFecha:
    array2 = montoInversor.split("-")
    monto.append(array2[0])
    fecha.append(array2[1])
montoInt = 0
montosEnListaInt = []
for mount in monto:
    montoInt = mount.split("$")
    montosEnListaInt.append(montoInt[1])
fechaArmador = ""
fechaWithOutString = []
for fe in fecha:
    fechaArmador = fe.split(":")
    fechaWithOutString.append(fechaArmador[1])

dia = []
mes = []
año = []
armadorString = ""
for fechaParaDivir in fechaWithOutString:
    armadorString = fechaParaDivir.split("/")
    dia.append(armadorString[0])
    mes.append(armadorString[1])
    año.append(armadorString[2])
montoMasGrande = 0
for precioInversion in range(len(montosEnListaInt)):
    if int(año[precioInversion]) == 2022:
        if montoMasGrande < float(montosEnListaInt[precioInversion]):
            montoMasGrande = float(montosEnListaInt[precioInversion])
print(f"la mayor inversion del 2022 fue de: ${montoMasGrande} ")

totalFondosInvertidos = 0
ListaSin0 = []
for m in mes:
    if m[0] == "0":
        ListaSin0.append(m[1])
    else:
        ListaSin0.append(m)
           

for varon in range(len(posicion)):
    if (sex[varon]) == "Male":
        if int(mes[varon]) <= int(ListaSin0[varon]) and int(año[varon]) == 2021:
            totalFondosInvertidos += float(montosEnListaInt[varon])
print(f"El total de fondos invertidos por varones en el segundo semestre del 2021 fue de ${totalFondosInvertidos}")
