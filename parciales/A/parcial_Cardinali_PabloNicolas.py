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


# 1) Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)
ciudad = input("Ingrese el nombre de una ciudad para buscar el inversor que vive allí: ")
nombreInversor = ""
listaInversoresOrdenada = [] # esta lista se usará para tener por separado cada dato de cada uno de los inversores de la primer lista
for inversor in inversores:
    listaInversoresOrdenada = inversor.split(",") #separaremos cada elemento de la lista original, en los elementos que separaba la ","
    if listaInversoresOrdenada[4] == ciudad: #en la ubicación 4 de la lista, se encuentra la ciudad a la que pertenece
        nombreInversor = listaInversoresOrdenada[1]

if nombreInversor == "":
    print("1) La ciudad ingresada, no se encontró en la lista. Intente nuevamente")
else: 
    print("1) El nombre de la persona que vive en", ciudad, "es:", nombreInversor)

# 2) Decir el monto de la mayor inversión realizada en el 2022.
inversionMayor = 0 #inicializo la variable con valor 0 para que ya la primer inversión encontrada, pase a ser la mayor hasta ese momento

for inversion in inversiones:
    if  int(inversion[-4:]) == 2022: #en esa pocision se encuentra el año de cada inversion y lo trabajo como entero
        montoInversion = float(inversion[8:17]) #en esta posición, está el monto de la inversión el cual es un valor flotante
        if montoInversion > inversionMayor:
            inversionMayor = montoInversion
inversionMayor = "$" + str(inversionMayor) #simplemente para visualizarlo mejor, convierto en string para poder agregarle el $
print("2) La mayor inversión del año 2022 fue de:", inversionMayor)

# 3) Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021 por inversores de sexo masculino.
totalInvertido = 0 
i = 0 #asigno esta variable para poder recorrer la lista de inversores en el for siguiente
for inversion in inversiones:
    if inversores[i].find(",Male,") > 0: #busca en la lista de inversores los que son hombres. Si son mujeres, el find da como resultado -1
        if  int(inversion[-4:]) == 2021 and int(inversion[-7:-5]) > 6: #analizo que pertenezca al segundo semestre del 2021
            totalInvertido = totalInvertido + float(inversion[8:17]) #tomo la inversión que cumpla la condicion y la sumo al total como número
    i = i + 1 #agrego 1 al valor de i para que en la siguiente vuelta, respete la posición entre las listas paralelas
totalInvertido = "$" + str(totalInvertido)
print("3) El total de fondos invertidos por varones en el segundo semestre del 2021 fue de", totalInvertido)
