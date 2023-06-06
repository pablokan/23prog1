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

""" Buscar el mail de cualquier inversor por nombre y mostrarlo. """

print('1)')

# 1) Buscar el correo de cualquier inversor por nombre y mostrarlo.
nombre_inversor = input("Ingrese el nombre de un inversor: ")

correo = None
for inversor in inversores:
    datos = inversor.split(",")
    if datos[1].lower() == nombre_inversor.lower():
        correo = datos[2]

if correo:
    print(f"El correo electrónico de {nombre_inversor} es: {correo}")
else:
    print(f"No se encontró un inversor con el nombre {nombre_inversor}")

print('2)')

inversiones = [374324.12,
423222.26,
591323.65,
279894.15,
884488.11,
136930.77,
925498.10,
634854.83,
682885.94,
748880.01,
490253.97,
953863.00,
473316.46,
193841.90,
325836.11,
632385.67,
137358.07,
320210.52,
558827.34,
140948.04]
inversionesTotales = 0
for inversion in inversiones:
    inversionesTotales += inversion
print("Cantidad de inversiones realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino:", inversionesTotales)

# 3) Saber cuántas inversiones fueron realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino.
print('3)')
inversiones_primer_semestre_2022 = [inversion for inversion in inversiones if '/2022' in inversion.split(':')[1] and int(inversion.split('/')[1]) <= 6]
inversiones_femeninas_primer_semestre_2022 = [inversion for inversion in inversiones_primer_semestre_2022 if 'Female' in inversores[int(inversion.split(',')[0])-1].split(',')]

cantidad_inversiones_femeninas_primer_semestre_2022 = len(inversiones_femeninas_primer_semestre_2022)

print("Cantidad de inversiones realizadas durante el primer semestre del año 2022 por inversoras de sexo femenino:", cantidad_inversiones_femeninas_primer_semestre_2022)