#Práctico 01, ejercicio pre-parcial

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

#inicial y apellido

nombre_mas_largo = ""

for nombre in nombres:
    apellido, nombre = nombre.split(", ")
    print (nombre[0],".", apellido)

#nombre más largo

    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre



print ("El nombre mas largo es: ", nombre_mas_largo)


#obtención de edades
edades=[]

for x in fechas:
    dia, mes, año = x.split("/")
    año = int(año)
    edades.append(2023-año)

print (edades)

#promedio de edades de mujeres

##cantidad_mujeres = 0

edad_total_mujeres = 0

for s in sexos: #error de acceso a la lista por indice erroneo
    if s == "f":
        cantidad_mujeres += 1
        edad_total_mujeres += edades[i]
print ("El promedio total de edades femeninas es: ", (edad_total_mujeres/cantidad_mujeres))









            




