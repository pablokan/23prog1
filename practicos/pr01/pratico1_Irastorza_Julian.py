#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
#2) Decir cuál es el nombre de pila más largo.
#3) Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)


nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"] 
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]


apellido=nombres
nombre=nombres

print("Iniciales y apellido de las personas: ")

for nombre in nombres:
    apellido, nombre_completo = nombre.split(", ")
    iniciales = ""
    partes_nombre = nombre_completo.split()
    for parte in partes_nombre:
        iniciales += parte[0] + "."
    iniciales = iniciales[:2]
    print(iniciales, apellido)

soloNombres= nombres
soloNombres = ["Kate", "Benicio", "Susana", "Carlos", "Azul", "Walter"]

nombreMasLargo = max(soloNombres, key=len)

print("El nombre de pila más largo es:", nombreMasLargo)

