# Diagnostico 1

nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"]

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



for nombre in nombres:
    apellido, nombre = nombre.split(", ")
    letra = nombre[0]
    print(f"{letra}. {apellido}")

nombreContador = ""
for nombre in nombres:
    apellido, nombre = nombre.split(", ")
    if len(nombre) > len(nombreContador):
        nombreContador = nombre
print("El nombre mas largo de la lista es: ", nombreContador) 

aH = 2023
mH = 5
dH = 17

edades = []
for fecha in fechas:
    dN, mN, aN= fecha.split("/")
    dN = int(dN)
    mN = int(mN)
    aN = int(aN)

    edad = aH - aN
    if (mN > mH) or ((mN == mH) and (dN > dH)):
        edad -= 1
    edades.append(edad)
    promedioEdad = sum(edades) / len(edades)

print(f"el promedio de edades es: {promedioEdad} ") 
