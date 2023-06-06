# Buscar el mail de cualquier inversor por nombre y mostrarlo.
# Obtener el total de todas las inversiones realizadas en el año 2021
# Saber cuantas inversiones fueron realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino.
 
# Salidas esperadas:
# El mail de Fionna es: fshanksterb@mashable.com
# Total de fondos del año 2021: $1679920.33
# Cantidad de inversiones de mujeres en el primer semestre del 2022: 4


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


nombreB = input("Ingrese el nombre de el mail que quiere buscar: ")

for inversor in inversores:
    numCl, nombre, mail, generos, ciudad = inversor.split(",")
    if nombreB == nombre:
        print(f"El correo electronico de {nombreB} es: {mail}")
    

acumInvers = 0
for invers in inversiones:
    dato1, dato2 = invers.split("-")
    fecha, fechaNum= dato2.split(":")
    dia, mes, año = fechaNum.split("/")
    monto1, monto2 = dato1.split("$")
    monto2 = float(monto2)
    if año == "2021":
        acumInvers += monto2
print(f"El monto total de inversiones realizadas en 2021 es de: {acumInvers}")

# Saber cuantas inversiones fueron realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino.

generos=[]
anios=[]
meses=[]
for inversor in inversores:
    numCl, nombre, mail, genero, ciudad = inversor.split(",")
    generos.append(genero)

for inversion in inversiones:
    monto,fecha = inversion.split("-")
    fechas=(fecha[7:])
    dia,mes,anio=fechas.split("/")
    meses.append(mes)
    anios.append(anio)
 
contador=0
y=0
for femenino in generos:
    if femenino=="Female" and anios[y]=="2022" and int(meses[y])>0 and int(meses[y])<7:
        contador+=1
    y+=1


print (f"La cantidad de mujeres que invirtieron en el primer semestre de 2022 es de: {contador}")