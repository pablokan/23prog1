nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana",  "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"] 

sexos = ["f","f","m","f","m","f","m"]

fechas = ["02/05/1943", "07/09/1984", "10/02/1971", "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]

# Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
for x in range(len(nombres)):
    for i in nombres:
        coma = i.split(", ")
        nombre = nombres[0]
        print(nombre, coma)

# Decir cuál es el nombre de pila más largo.

# Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom).
mujeres = []
for x in range(len(sexos)):
    if sexos[x] == "f":
        mujeres.append(sexos[x])
print(mujeres)


fechasMujeres = []
f1 = ""
f2 = ""
f3 = ""
f4 = ''
fechasM = f1 + f2 + f3 + f4
for x in range(len(fechas)):
    f1 = fechas[0]
    f2 = fechas[1]
    f3 = fechas[3]
    f4 = fechas[5]
    fechasMujeres.append(fechasM)
print(f1)


