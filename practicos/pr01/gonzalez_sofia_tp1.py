#Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
#Decir cuál es el nombre de pila más largo.
#Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)

nombres = []
"Torres, Ana", "f", "02/05/1943"
"Hudson, Kate", "f", "07/09/1984"
"Quesada, Benicio", "m", "10/02/1971"
"Campoamores, Susana", "f", "21/12/1967"
"Santamaría, Carlos", "m", "30/01/1982"
"Skarsgard, Azul", "f", "30/08/1995"
"Catalejos, Walter", "m", "18/07/1959"

#1
for i in range(len(nombres)):
    apellido = nombres[7]
    print(apellido[0:7])

#2
nombres = [i]
"Torres, Ana",
"Hudson, Kate",
"Quesada, Benicio",
"Campoamores, Susana", 
"Santamaría, Carlos",
"Skarsgard, Azul", 
"Catalejos, Walter"


for i in range (len(nombres)):
    print(nombres)[i]
print("el nombre mas largo es:", nombres[1])


#3 
sexos = ["f","f","m","f","m","f","m"]
fechas = [i]
"02/05/1943",
"07/09/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"


