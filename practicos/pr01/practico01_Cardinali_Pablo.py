datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/09/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",]

# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

separador = 0 # posicion donde se separa apellido del nombre
inicialMasApellido = ""
print("1) La lista de personas ingresadas es: ")
for persona in datos:
    separador = persona.find(", ")+2
    inicialMasApellido = persona[separador:separador + 1] + ". " + persona[:separador-2]
    print(inicialMasApellido)

# 2) Decir cuál es el nombre de pila más largo.

largoNombre = 0
finalNombre = 0 # aquí se pondrá la posición donde termina el nombre de pila
nombreLargo = ""
for persona in datos:
    separador = persona.find(", ")+2
    finalNombre = persona.find(", ", separador) # volvemos a buscar pero empezando luego del apellido
    if len(persona[separador:finalNombre]) > largoNombre:
        largoNombre = len(persona[separador:finalNombre])
        nombreLargo = persona[separador:finalNombre]
print("2) El nombre más largo es:", nombreLargo, "con", largoNombre, "letras.")

# 3) Mostrar el promedio de edad de las mujeres.

aHoy = 2023
mHoy = 5
dHoy = 17
aMujer = 0
mMujer = 0
dMujer = 0
cantMujeres = 0
sumaEdades = 0
for persona in datos:
    if persona.find(" f, ")>0: 
        cantMujeres += 1
        aMujer = int(persona[-4:])
        mMujer = int(persona[-7:-5])
        dMujer = int(persona[-10:-8])
        edad = aHoy - aMujer
        if (mMujer > mHoy) or ((mMujer == mHoy) and (dMujer > dHoy)):
             edad -= 1
        sumaEdades += edad
promedioEdadMujeres = sumaEdades/cantMujeres
print("3) El promedio de edad de las mujeres es:", promedioEdadMujeres)

