datos = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/09/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]

# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

print("1) Iniciales y apellido de las personas:")
for arreglo in datos:
    nombreApellido = arreglo[0].split(', ')
    print(nombreApellido[1][0] + ".", nombreApellido[0])
    
# 2) Decir cuál es el nombre de pila más largo.
nombreLargo = ""
for arreglo in datos:
    nombre = arreglo[0].split(", ")[1]
    if(len(nombre) > len(nombreLargo)):
        nombreLargo = nombre
print("2) El nombre más largo es:", nombreLargo)

# 3) Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)
dHoy = 15
mHoy = 5
aHoy = 2023
counterEdades = 0
cantMujeres = 0
for arreglo in datos:
    genero = arreglo[1]
    if genero == "f":
        cantMujeres += 1
        arregloFechaNac = arreglo[2].split("/")
        dNac = int(arregloFechaNac[0])
        mNac = int(arregloFechaNac[1])
        aNac = int(arregloFechaNac[2])
        a = aHoy - aNac
        if((mNac > mHoy) or (mNac == mHoy and dNac > dHoy)):
            a -= 1
        counterEdades += a
        
print("3) El promedio de edad de las mujeres es:", counterEdades/cantMujeres)