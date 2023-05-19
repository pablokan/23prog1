nombre = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"] 
personas = []
nombres = []
apellido = []
sexos = ["f","f","m","f","m","f","m"]
fechas = [
"02/05/1943",
"07/09/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]

for name in nombre:
    personas = name.split(",")
    nombres.append(personas[1])
    apellido.append(personas[0])

for name in range(len(nombres)):
    nombreTemporal = nombres[name]
    print(nombreTemporal[1:2],". ", apellido[name])

nombreLargo = ""
for name in nombres:
    if len(name) > len(nombreLargo):
        nombreLargo = name

print("El nombre mas largo es:", nombreLargo)

fechaTemporal = []
edades = []
edadTemporal = 0

for edad in range(len(fechas)):
    if sexos[edad] == "f":
        fechaTemporal = fechas[edad]
        dia = fechaTemporal[0:2]
        dia = int(dia)
        mes = fechaTemporal[3:5]
        mes = int(mes)
        ano = fechaTemporal[6:10]
        ano = int(ano)
        edadTemporal = (2023 - ano) 
        if 5 - mes < 0 or 5 - mes == 0 and 17 - dia < 0:
            edadTemporal = edadTemporal - 1
        edades.append(edadTemporal)


sumaEdades = 0
for i in range(len(edades)):
    sumaEdades = sumaEdades + edades[i]

promedio = sumaEdades // len(edades)
print("El promedio de edades de las mujeres es de: ", promedio)





