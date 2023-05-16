#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido 
#completo de todas las personas.
#2) Decir cuál es el nombre de pila más largo.
#3) Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)

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



#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido 
#completo de todas las person
inicialap = []
for nombre in nombres:
  nombre, apellido = nombre.split(",")
  inicial = nombre[0] + "."
  inicialapellido = inicial + " " + apellido
  inicialap.append(inicialapellido) 
print(inicialap)

#2) Decir cuál es el nombre de pila más largo.

maslargo = ""
cantLetras= 0
for nombre in nombres:
  apellido, nombre = nombre.split(",")
  largo = len(nombre)
  if largo > cantLetras:
    maslargo = nombre
    cantLetras = largo
print("el nombre mas largo es",maslargo, "este tiene", cantLetras, "letras")

#3) Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)

edades = []
totalm = 0
añoactual =2023
for x in range(len(sexos)):
    if sexos[x] == "f":
      totalm += 1 
#for i in range(len(fechas)):
 #   if fechas[i] != "/":
  #     edades.append(fechas[i])no sale

print(totalm)#totalizo para sacar prom


      
        
        