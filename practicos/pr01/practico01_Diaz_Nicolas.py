#Mostrar las iniciales de los nombres con un punto, 
# luego un espacio y finalmente el apellido completo de todas las personas.

nombres = ["Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
]

nombres_iniciales = []

for nombre in nombres:
    partes_nombre = nombre.split()
    inicial_nombre = partes_nombre[0][0] + '.'
    apellido_completo = partes_nombre[-1]
    nombre_completo = inicial_nombre + ' ' + apellido_completo
    nombres_iniciales.append(nombre_completo)

print("Inciales y apellidos de las personas:  ",nombres_iniciales)

#Decir cuál es el nombre de pila más largo.

nombres = ["Ana","Kate","Benicio","Susana","Carlos","Azul","Walter"]

nombre_mas_largo = ""

for nombre in nombres:
    partes_nombre = nombre.split()
    for parte in partes_nombre:
        if len(parte) > len(nombre_mas_largo):
            nombre_mas_largo = parte

print("El nombre de pila más largo es:", nombre_mas_largo)

#Mostrar el promedio de edad de las mujeres

fechas = [
"02/05/1943",
"07/09/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]


aH = 1995
mH = 8
dH = 30
aN = 1943
mN = 5
dN = 2

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1

print("El promedio de la edad:",edad)

