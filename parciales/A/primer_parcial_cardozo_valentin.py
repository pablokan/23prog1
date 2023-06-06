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


# Ejercicio 1: Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)
keepGoing = input('Desea buscar un inversor por ciudad? [si/no]: ')
while keepGoing == 'si':
    findCity = input('Ingrese nombre de la ciudad: ')
    findName = ''
    for inversor in inversores:
        data = inversor.split(',')
        city = data[4]
        name = data[1]

        if city == findCity:
            findName = name

    print('El nombre de la persona que vive en ' + findCity + 'es: ' + findName)
    keepGoing = input('Desea continuar buscando? [si/no]: ')

# Ejercicio 2: Decir el monto de la mayor inversión realizada en el 2022
investmentYear = '2022'
mayorInvestment = 0
cents = 0

for inversion in inversiones:
    info = inversion.split('-')
    infoAmount = info[0].split(': ')
    infoDate = info[1].split(':')
    date = infoDate[1].split('/')

    if date[2] == investmentYear:
        amount = infoAmount[1][ infoAmount[1].find('$') + 1 :]
        if float(amount) > mayorInvestment:
            mayorInvestment = float(amount)

print('La mayor inversión del año ' + investmentYear + 'fue de: $' + str(mayorInvestment))
    
# Ejercicio 3: Obtener el total de inversiones que fueron realizadas durante el segundo semestre
# del año 2021 por inversores de sexo masculino.
searchYear = '2021'
initMonth = '06'
endMonth = '12'
searchSex = 'Male'
totalInvestment = 0
cents = 0

for inversor in inversores:
    data = inversor.split(',')
    sex = data[3]
    
    if sex == searchSex:
        index = int(data[0]) - 1

        info = inversiones[index].split('-')
        infoAmount = info[0].split(': ')
        infoDate = info[1].split(':')
        date = infoDate[1].split('/')

        if date[2] == searchYear and date[1] >= initMonth and date[1] <= endMonth:
            amount = infoAmount[1][ infoAmount[1].find('$') + 1 :].split('.')
            totalInvestment = totalInvestment + int(amount[0])
            cents = cents + int(amount[1])

totalInvestment = totalInvestment + (int(cents) / 100)
print('El total de fondos invertidos por varones en el segundo semestre del 2021 fue de $' + str(totalInvestment))