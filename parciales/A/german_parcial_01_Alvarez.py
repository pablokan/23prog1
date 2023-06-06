# El siguiente codigo corresponde a la respuesta del primer parcial del alumno Alvarez Germán(40928479) el dia 31 de mayo de 2023.
# El mismo responde a las siguientes consignas:
# - Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)
# - Decir el monto de la mayor inversión realizada en el 2022.
# - Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021 por inversores de sexo masculino.

investors = [
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

investments = [
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

numbers = []
names = []
mails = []
gender = []
cities = []

# Pre procesamiento de datos
# Para cada fila de datos de inversores, divido la informacion por el caracter ',' y populo los arreglos de numero, nombre, mail, genero y ciudad
for dataInversor in investors:
    splitted = dataInversor.split(',')

    numbers.append(splitted[0])
    names.append(splitted[1])
    mails.append(splitted[2])
    gender.append(splitted[3])
    cities.append(splitted[4])

# Para cada fila de datos de inversiones, divido la informacion por el caracter ',' y populo los arreglos de monto y fecha
investedAmounts = []
investedDates = []
for dataInvestment in investments:
    splitted = dataInvestment.split(' - ')

    investedAmount = splitted[0][len('Monto: $'):]
    investedAmounts.append(investedAmount)

    investedDate = splitted[1][len('Fecha:'):]
    investedDateSplitted = investedDate.split('/')
    investedDates.append(investedDateSplitted)

# 1) Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)

# Solicito al usuario el nombre de una ciudad
investorCity = input("Ingrese ciudad de inversion: ")
investorName = ''

# Busco entre todos los inversores si hay una coincidencia respecto a la ciudad. Si la hay, guardo su valor
for i in range(len(numbers)):
    if cities[i] == investorCity:
        investorName = names[i]

print(f"1) El nombre de la persona que vive en {investorCity} es: {investorName}")

# 2) Decir el monto de la mayor inversión realizada en el 2022.

# Analizo las inversiones y si fueron en el año 2022 y supera el maximo almacenado, lo guardo como maximo
maxAmount2k22 = 0
for i in range(len(investedAmounts)):
    yearOfInvested = int(investedDates[i][2])
    cleanAmount = float(investedAmounts[i])

    if yearOfInvested == 2022 and cleanAmount > maxAmount2k22:
            maxAmount2k22 = cleanAmount

print(f"2) La mayor inversión del año 2022 fue de: ${maxAmount2k22}")

# 3) Obtener el total de investments que fueron realizadas durante el segundo semestre del año 2021 por inversores de sexo masculino.
# Analizo los inversores y su genero es masculino, e inviritó en 2021, sumo su valor al acumulador
totalMaleInvestment = 0
for i in range(len(investedAmounts)):
    yearOfInvested = int(investedDates[i][2])
    cleanAmount = float(investedAmounts[i])

    if yearOfInvested == 2021 and gender[i] == 'Male':
            totalMaleInvestment += cleanAmount

print(f"3) El total de fondos invertidos por varones en el segundo semestre del 2021 fue de ${totalMaleInvestment}")
