'''Procesos para las salidas:

1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

2) Decir cuál es el nombre de pila más largo.

3) Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)


Realizar tres procesos separados!
(Pueden hacer 4 procesos si les parece conveniente en primer lugar obtener los nombres y apellidos separados y almacenarlos en listas)
'''

nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"]

sexos = ["f","f","m","f","m","f","m"]

fechas = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]


individuos=[]
nombres2 = []
for i in nombres:
    individuo = i.split(",")
    individuos.append(individuo)
    nombres2.append(i[0]+". "+ individuo[1] )
print(nombres2)



soloNombre = []
for i in individuos:
    soloNombre.append(i[1])
print(soloNombre)

nombreMasLargo = ""
letras= 0
for nombre in soloNombre:
    letras = len(i)
    nombreMasLargo = i
    if len(i) > letras:
        nombreMasLargo = i
    else:
        continue
print("el nombre mas largo es", nombreMasLargo)


print("el nombre mas largo es " , max(soloNombre)) #lo puse asi porque no pude de otra forma!! como para hacer algo

#Al punto 3 no llegue!!! =( 
    



 


