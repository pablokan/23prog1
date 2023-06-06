'''
Enunciado:

Tengo dos listas paralelas de clientes de Fondos de Inversión. 
La primera lista tiene un número de cliente, su nombre, mail, sexo y ciudad.
La segunda lista tiene el monto de la inversión y la fecha de la misma.

Quiero hacer lo siguiente:

1) Buscar el nombre de cualquier inversor por ciudad y mostrarlo. (Las ciudades no se repiten)
2) Decir el monto de la mayor inversión realizada en el 2022.
3) Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021 por inversores de sexo masculino.


Salidas esperadas:
El nombre de la persona que vive en Dongping es: Micky
La mayor inversión del año 2022 fue de: $884488.11
El total de fondos invertidos por varones en el segundo semestre del 2021 fue de $1090793.77
'''


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

ciudad = "Champaign"
inversorBuscado = ""

for inversor in inversores:
    datos = inversor.split(",")
    # print(datos[4])
    if datos[4] == ciudad:
        # print(datos[1])
        inversorBuscado= datos[1]
    
print(f'El nombre de la persona que vive en {ciudad} es {inversorBuscado}')



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


'''2) Decir el monto de la mayor inversión realizada en el 2022.'''


# datos=[]
# importeMaximo = 0

# for inversion in inversiones:
#     datos = inversion.split(" - ")
#     # print(datos)
#     fecha = datos[1]
#     monto = datos[0]
#     # print(fecha)
#     indiceAño = fecha.find("202")
#     año= fecha[indiceAño:]
#     # # print(año)
#     # print(monto)
#     indiceImporte= monto.find("$")
#     importe = float(monto[indiceImporte+1:])
#     # print(importe)
#     if año == "2022":
#         if importe > importeMaximo:
#             importeMaximo = importe

# print(f'La mayor inversión del año 2022 fue de: {importeMaximo}')
        
    
'''3) Obtener el total de inversiones que fueron realizadas durante el segundo semestre del año 2021 por inversores de sexo masculino.'''


sexos=[]
for inversor in inversores:
    datos = inversor.split(",")
    # print(datos[3])
    sexos.append(datos[3])
# print(sexos)



datos=[]
importeMaximo = 0
sumaImporte = 0
importes = []
pesos=[]
for inversion in inversiones:
    datos = inversion.split(" - ")
    # print(datos)
    fecha = datos[1]
    monto = datos[0]
    # print(fecha)
    indiceAño = fecha.find("202")
    año= fecha[indiceAño:]
    indiceMes = fecha.find(":")
    mes = int(fecha[indiceMes+4:indiceMes+6])
    # print(mes)
    # # print(año)
    # print(monto)
    indiceImporte= monto.find("$")
    importe = float(monto[indiceImporte+1:])
    # print(importe)
    if año == "2022":
        if importe > importeMaximo:
            importeMaximo = importe
    if año == "2021":
        importes.append(importe)
    for valor in importes:
        pesos.append(valor)
        

# print(pesos)
# print(importes)

print(f'La mayor inversión del año 2022 fue de: {importeMaximo}')
totalInversiones = 0
for i in range(len(sexos)):
    # print(sexos[i])
    if sexos[i] == "Male":
        totalInversiones += pesos[i]
print(f'El total de fondos invertidos por varones en el segundo semestre del 2021 fue de {totalInversiones}')