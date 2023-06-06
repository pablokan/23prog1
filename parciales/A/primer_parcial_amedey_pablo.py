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
# número de cliente, su nombre, mail, sexo y ciudad.
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
nuevaLista = [] # Lista vacia a la que se le van a cargar sublistas. Se cargaran los datos de los inversores
print('Ingrese la ciudad de la persona que desea buscar')
ciudad = input('Besançon-Jawand-Rîbniţa-Tlogoagung-Tonjongsari-Xianning-Dongping-Perm-Champaign-Normanton-Serra-Ccuntuma-Shihua-Huangtan-Sehwān-Buenavista-Maclear-Kebon-Gimry-Bungoma\n')
for i in range(len(inversores)): 
    inversor = inversores[i].split(',') # Divide la cadena dentro de la posicion actual lista
    nuevaLista.append(inversor) # Lo agrega a una nueva lista
# Dentro de la lista se crean sublustas de este estilo ['1', 'Veriee', 'vvasilkov0@qq.com', 'Female', 'Besançon']
for i in range(len(nuevaLista)):
    if ciudad == nuevaLista[i][-1]:
        nombre = nuevaLista[i][1]
print('El nombre de la persona que vive en ' + ciudad + ' es: ' + nombre )
montos = []
listaDeFechas = []
for i in range(len(inversiones)):
    posSignoPeso = inversiones[i].find('$')
    posEspacio = inversiones[i].find(' ', posSignoPeso)
    posDosPuntos = inversiones[i].find(':', posSignoPeso)
    monto = inversiones[i][posSignoPeso+1:posEspacio]
    fecha = inversiones[i][posDosPuntos+1:]
    montos.append(float(monto))
    listaDeFechas.append(fecha)
fechas = []
for i in range(len(listaDeFechas)):
    fecha = listaDeFechas[i].split('/')
    fechas.append(fecha)
añosEnenteros = [] # Transformo los años en enteros
mesesEnEnteros = [] # Transformo los meses en enteros
for i in range(len(fechas)):
    año = int(fechas[i][2]) 
    mes = int(fechas[i][1]) 
    añosEnenteros.append(año)   
    mesesEnEnteros.append(mes)
monto = 0
for i in range(len(montos)):
    if añosEnenteros[i] == año:
        if montos[i] > monto:
            monto = montos[i]
print('La mayor inversión del año ' + str(año) + ' fue de: $' + str(monto))
año = 2021
mes = 7
total = 0
for i in range(len(añosEnenteros)):
    if añosEnenteros[i] == año and mesesEnEnteros[i] >= mes and nuevaLista[i][3] == 'Male': 
        total += montos[i]
print('El total de fondos invertidos por varones en el segundo semestre del ' + str(año) + ' fue de $' + str(total))

