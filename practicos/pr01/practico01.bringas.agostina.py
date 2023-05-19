# Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas 
# las personas.
# Decir cuál es el nombre de pila más largo.
#Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)
# aH = 2023
"""mH = 5
dH = 3
aN = 2000
mN = 2
dN = 21

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1

print(edad)"""

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


#1)
nombres=[]
apellido=["Torres", "Hudson", " Quesada", "Campoamores", "Santamaria", "Skarsgard", "Catalejos"]
cantidad=len(nombres)
for i in range( len(nombres)):
    nombres.remove[apellido]
    print(nombres[i])
    
    """apellido + datos[1]
    print(apellido(0:1))
    principio=dato[:1]
    print(dato[])
    print(datos[0:1])"""

#2)Decir cuál es el nombre de pila más largo.
for i in range (len(nombres)):
    print(nombres[i]) 
    print("el apellidos mas largo es: ", nombres[i])


#3)#Mostrar el promedio de edad de las mujeres.
contador=0
nombres=[]
cantidad=len(fechas)
if sexos =="f" and sexo==fechas:
    for i in range(fechas):
   
        contador=cantidad[i] + contador
        promedio=cantidad/contador
        print("promedio de mujeres", promedio )