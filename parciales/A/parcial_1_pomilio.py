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
print('=' * 50)
#datos
inversorIndividual = ''

datos = ''
numeroDeInversor = ''
nombreDeInversor = ''
mailDeInversor = ''
sexoDeInversor = ''
ciudadDeInveror = ''

#buscar inversor por ciudad
nombres = []
ciudades = []
sexos = []

for elemento in inversores:
    inversorIndividual = elemento.split(',')
    
    numeroDeInversor = inversorIndividual[0]
    nombreDeInversor = inversorIndividual[1]
    mailDeInversor = inversorIndividual[2]
    sexoDeInversor = inversorIndividual[3]
    ciudadDeInveror = inversorIndividual[4]
    
    
    sexos.append(sexoDeInversor)

    nombres.append(nombreDeInversor)
    ciudades.append(ciudadDeInveror)


insertarCiudad = input('Inserte la ciudad => ').title()

for i in range(len(nombres)):
    if insertarCiudad == ciudades[i]:
        print(f'El inversor que vive en {insertarCiudad} es: {nombres[i]}')

print('=' * 50)
#datos inversiones
inversionIndividual = ''

monto = ''
fecha = ''

fechasSeparadas = ''
dia = ''
mes = ''
año = ''

años = []
montoTotal = []
meses = []

for elemento in inversiones:
    inversionIndividual = elemento

    monto, fecha = inversionIndividual.split('-')

    dia, mes, año = fecha.split('/')
    años.append(año)
    meses.append(mes)

    posDePeso = monto.find('$')
    numeroMonto = monto[posDePeso + 1:]

    montoTotal.append(numeroMonto)


montoMasGrande = 0

for i in range(len(montoTotal)):
    montoTotal[i] = float(montoTotal[i])
    
    if años[i] == '2022':
        if montoTotal[i] > montoMasGrande:
            montoMasGrande = montoTotal[i]

print(f'El monto mas grande de 2022 es: {montoMasGrande}')

print('=' * 50)
#inversores masculinos

personaIndividual = ''



#sexos
#nombres
#meses
#años
intMeses = []
intMontos = []

for i in range(len(montoTotal)):
    monto = float(montoTotal[i])
    intMontos.append(monto)

for i in range(len(meses)):
    mes = float(meses[i])
    intMeses.append(mes)

totalInvertidoSegundoSemetro2021 = 0

for i in range(len(sexos)):
    if sexos[i] == 'Male':
        if años[i] == '2021':
            if intMeses[i] >= 6:
                totalInvertidoSegundoSemetro2021 += intMontos[i]

print(f'La inversion total de Hombres en el segundo semetres de 2021 es de: {totalInvertidoSegundoSemetro2021}')
print('=' * 50)