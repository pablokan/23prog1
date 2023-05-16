#Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
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

soloNom = [' '.join(nombre.split()[1:2]) for nombre in nombres]

#Realizo el primer proceso, mostrar las iniciales con un punto, luego un espacio y finalmente el apellido correspondiente
inicialApellido = []
inicial = []
apellido = []
for i in range(len(soloNom)):
    for a in range(len(soloNom[i])):
        if a == 0:
            inicial.append(soloNom[1])
print(inicial)
#FALTA TERMINAR

#Realizo el segundo proceso, buscar el nombre mas largo
nombreActual = int(0)
nombreLargo = int(0)
for i in range(len(soloNom)):
    contador = 0
    for a in range(len(soloNom[i])):
        contador = contador + 1
    nombreActual = contador
    if nombreActual >= nombreLargo:
        nombreLargoMostrar = soloNom[i]
        nombreLargo = contador
    else:
        nombreLargoMostrar = nombreLargoMostrar
        
print(nombreLargoMostrar)
#Segundo proceso Funciona
        
#Realizo el tercer proceso, mostrar el promedio de edad de las mujeres  

#FALTA TERMINAR






