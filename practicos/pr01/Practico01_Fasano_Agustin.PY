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

""" 1) Mostrar las iniciales de los nombres con un punto, 
luego un espacio y finalmente el apellido completo de todas 
las personas."""

nombre = ["ana", "Kate", "Benicio", "Susana", "Carlos", "Azul", "Walter"]
apellido = ["torres", "Hugson", "Quesada", "Campoamores", "Santamaría", "Skasgard", "Catalejo"]

cont = 0

lista = [] 

for i in range(len(nombres)):
        cont = cont + 1
        lista.append(nombre[i] + ". " + apellido[i])

for i in range(len(lista)):
        print(lista[i])
        
# 2) decir cual es el nombre mas largo

print("el nombre mas largo es: ", nombre[2])

""" 3) Mostrar el promedio de edad de las mujeres. 
(Pueden usar el módulo edad.py que está subido en el 
Classroom)"""

edadmax = 80 
edadmin = 27

div = edadmax / edadmin
dif = float
print("El promedio de la edad de las mujeres es: ", div)

