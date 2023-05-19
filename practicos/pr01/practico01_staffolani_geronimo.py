#Practico 1: Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
#Decir cuál es el nombre de pila más largo.
#Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)

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

for nombre in nombres:
    apellido, nombre = nombre.split(", ")
    letra = nombre[0]
    print(f"{letra}. {apellido}")
 
print("-----------------------------------Comienzo act 2------------------------------------")

nombreLargo = ""
for nombre in nombres:
    apellido, nombre = nombre.split(", ")
    if len(nombre) > len(nombreLargo):
        nombreLargo = nombre

print("El nombre más largo de la lista es: ", nombreLargo) 
 
print("-----------------------------------Comienzo act 3------------------------------------")



for años in fechas:
    aH = 2023
    mH = 5
    dH = 17
    dia, mes, año = años.split("/")
    
    aN = int(año)
    mN = int(mes)
    dN = int(dia)
    edad = aH-aN
    if (mN > mH) or ((mN == mH) and (dN > dH)):
        edad -= 1
        
        print(edad)



