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

# Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)

name=[]
city=[]
sexos= []
for persona in inversores:
    perso= persona.split(",")
    name.append(perso[1])
    city.append(perso[4])
    sexos.append(perso[3])
preguntarLaCiudad= input("ingrese ciudad: ")
contar= -1
for ciudad in city:
    contar = contar + 1
    if ciudad == preguntarLaCiudad:
        print("el nombre de la persona que vive en", preguntarLaCiudad,"es: ", name[contar])


#Decir el monto de la mayor inversión realizada en el 2022.


montos=[]
fechas=[]
anios=[]
mes=[]
masAlto= 0
for dividir in inversiones:
    division = dividir.split(" - Fecha:")
    fechas.append(division[1])
    divisionMontos = division[0].split("$")
    montos.append(divisionMontos[1])
for anio in fechas:
    n = anio.split("/") 
    anios.append(n[2])  
    mes.append(n[1])
contar=-1
for i in anios:
    contar = contar + 1
    if i == "2022":
        Alto= float(montos[contar])
        if masAlto < Alto:
            masAlto= Alto
print("La mayor inversion del anio 2022 fue de : $", masAlto)

# Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021
# por inversores de sexo masculino.

inversiones_totales=0
vuelta = -1
inversionTotal=0
posicionMasc=[]

for i in range(len(inversores)):
    datos_inversor = inversores[i].split(",")
    sexo = datos_inversor[3]
    
    if sexo == "Male":
        fechaDeInversion = inversiones[i].split("Fecha:")[1]
        mes= int(fechaDeInversion.split("/")[1])
        anio = int(fechaDeInversion.split("/")[2])
        if anio == 2021 and mes >= 7:
         inversiones_totales = inversiones_totales + float(montos[i])
        
        
print("El total de fondos invertidos por varones en el segundo semestre del 2021 fue de : $", inversiones_totales)