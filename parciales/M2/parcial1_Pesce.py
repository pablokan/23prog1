""" Quiero hacer lo siguiente:

Buscar el mail de cualquier inversor por nombre y mostrarlo.
Obtener el total de todas las inversiones realizadas en el año 2021
Saber cuantas inversiones fueron realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino.


Salidas esperadas:
El mail de Fionna es: fshanksterb@mashable.com
Total de fondos del año 2021: $1679920.33
Cantidad de inversiones de mujeres en el primer semestre del 2022: 4
 """


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

mailR = ""
t = 0
totalF = 0
woman = 0
listW = []

find = input("Enter the name of the investor you want to search: ")

#Ciclo para buscar el mail de la persona ingresada (Aproveche el recorrido y a cada persona femenina le saque el id y lo agregue a una lista nueva para utilizarlos en el tercer ciclo)

for data in inversores:
    num, name, mail, gender, city = data.split(",")
    if find == name:
        mailR = mail
        t = 1
    if gender == "Female":
        listW.append(num)

if t == 1:
    print(f"1) {find}'s email is: {mail}")
else:
    print("1) The name entered is not in the list of investors")


#Ciclo para obtener el total de inversiones en el 2021

for data1 in inversiones:
    inf, inf1 = data1.split("-")
    date, date1= inf1.split(":")
    day, month, year = inf1.split("/")
    aux, mount = inf.split("$")
    mount = float(mount)
    if year == "2021":
        totalF = totalF + mount

totalF = round(totalF,2)

print(f"2) The total amount of investments made in 2021 is: ${totalF}")


#Ciclo para contar la cantidad de mujeres inversoras en el primer semestre del 2022

for id in listW:
    id = int(id)
    inf_, inf1_ = inversiones[id-1].split("-")
    date_, date1_= inf1_.split(":")
    day_, month_, year_ = date1_.split("/")
    year_ = int(year_)
    month_ = int(month_)
    if year_ == 2022 and month_ <= 6:
        woman = woman + 1

print(f"3) The number of women's investments in the first half of 2022: {woman}")