nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 
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


nombre =[]
nombre1 = []
print("1) Inicial y aprellido de las personas: ")
for i in range(len(nombres)):
        nombre = nombres[i].split(",")
        for j in range(len(nombre)):
                nombre1 = nombre[j][1] + ". " + nombre[0]
        print(nombre1)

nombre =[]
nombre1 = []
Largo = 0
nombreLargo = ""
for i in range(len(nombres)):
        nombre = nombres[i].split(", ")
        for j in range(len(nombre)):
                nombre1 = nombre[j]
        if Largo < len(nombre1):
                Largo = len(nombre1)
                nombreLargo = nombre1
print("2) El nombre mas largo es: ",nombreLargo)
        
suma = 0
añoHoy = 2023
mesHoy = 5
diaHoy = 17
for i in range(len(fechas)):
        if int(fechas[i].split("/")[1]) > mesHoy or int(fechas[i].split("/")[1])==mesHoy and int(fechas[i].split("/")[0]) > diaHoy:
                edad = añoHoy - int(fechas[i].split("/")[2])-1 
        else:
                edad =  añoHoy - int(fechas[i].split("/")[2])
        suma = (suma + edad)
print("3) La edad promedio es: ", int(suma/len(fechas)))


