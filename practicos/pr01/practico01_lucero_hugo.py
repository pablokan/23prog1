nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter" ]
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]

#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

for i in range(len(nombres)):             #un elemento por linea
    for j in nombres:
        coma = j.split(", ")                  #divide ,si encuentra separa con ','
        n = nombres[0]  
        print(n,coma)
        
# recorte iniciales 
    
         

    

#2) Decir cuál es el nombre de pila más largo.



#3) Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)

mujeres = []
for i in range(len(sexos)):
    if sexos[i] == "f":
        mujeres.append(sexos[i])              #agrega a la lista vacia mujeres
print(mujeres)

fechasMujeres = []
f1 = ""
f2 = ""
f3 = ""
f4 = ""
fMujeres = f1 + f2 + f3 + f4
for i in range(len(fechas)):
    f1 = fechas[0]                             #"Torres, Ana"
    f2 = fechas[1]                             #"Hudson, Kate"
    f3 = fechas[3]                             #"Campoamores, Susana",
    f4 = fechas[5]                             #"Skarsgard, Azul"
    fechasMujeres.append(fMujeres)             #agrega a la lista vacia        
print(f1,f2,f3,f4)


#promedio de edad de mujeres es

a = 2023
m = 6
d = 3
a1 = 1973
m2 = 2
d3 = 21

edad = a - a1
if (m2 > m) or ((m2 == m)) and (d3 > d):
    edad -= 1
print(edad)




