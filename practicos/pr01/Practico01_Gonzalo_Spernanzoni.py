#Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
nombres = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana",
    "Santamaría, Carlos",
    "Skarsgard, Azul",
    "Catalejos, Walter"
]
sexos = ["f", "f", "m", "f", "m", "f", "m"]
fechas = [
    "02/05/1943",
    "07/09/1984",
    "10/02/1971",
    "21/12/1967",
    "30/01/1982",
    "30/08/1995",
    "18/07/1959"
]

for i in range(len(nombres)):
    nombre_completo = nombres[i]
    nombre_split = nombre_completo.split(", ")
    apellido = nombre_split[0]
    nombre = nombre_split[1]

    iniciales = ""
    if len(nombre) > 0:
        iniciales += nombre[0] + ". "

    print(iniciales,apellido) 
 




#Decir cuál es el nombre de pila más largo.
nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 
nombreMasLargo = ""

for nombreCompleto in nombres:
    nombreSeparados = nombreCompleto.split(", ")
    nombrePila = nombreSeparados[1]
    if len(nombrePila) > len(nombreMasLargo):
        nombreMasLargo = nombrePila
    
    
print(nombreMasLargo)


nombre_pila_mas_largo = ""

for nombre_completo in nombres:
    nombre_split = nombre_completo.split(", ")
    nombre_pila = nombre_split[1]

    if len(nombre_pila) > len(nombre_pila_mas_largo):
        nombre_pila_mas_largo = nombre_pila

print("El nombre de pila más largo es:", nombre_pila_mas_largo)
    
    #no entiendo lptm porque dan diferente