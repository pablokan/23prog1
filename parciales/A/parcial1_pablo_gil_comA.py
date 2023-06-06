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


print("1)")
entradaCiudad = "Buenavista"
for elem in inversores:
    ncliente, nombre, mail, sexo, ciudad = elem.split(",")
    posCiudad = elem.find(entradaCiudad)
    if posCiudad != -1:
        print("El nombre de la persona que vive en", ciudad, "es:", nombre)


print("-----------------------------------------------------------------------")
print("2)")
acum = 0
for elem in inversiones:
    monto, fecha = elem.split("-")
    inversion = monto.split("$")
    numeros = float(inversion[1])
    cadFecha = fecha[7:]
    dia, mes, año = cadFecha.split("/")
    if numeros > acum and año == "2022":
        acum = numeros
print("La mayor inversión del año 2022 fue de: $" + str(acum))


print("-----------------------------------------------------------------------")
print("3)")

fondos = 0
for rec in range(len(inversores)):
    var = inversores[rec]
    aux = inversiones[rec]
    montos, fechas = aux.split("-")
    cadFechas = fechas[7:]
    dia, mes, año = cadFechas.split("/")
    posAño = año.find("2021")
    posPeso = montos.find("$")
    ncliente, nombre, mail, sexo, ciudad = var.split(",")
    if sexo == "Male" and mes > "06" and posAño != -1:
        fondos += float(montos[posPeso+1:posPeso+10])
print("El total de fondos invertidos por varones en el segundo semestre del 2021 fue de: $"+ str(fondos))
