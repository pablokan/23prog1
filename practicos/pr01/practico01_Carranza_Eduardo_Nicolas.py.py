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


#   Apellido + Inicial nombre
print("Proceso 1")
print("")
c = -1
for i in range(len(nombres)):
    c = c + 1
    sub_nombre = nombres[c].split()
    nombre_solo = sub_nombre[1] 
    apellido_solo = sub_nombre[0]
    posicion_coma = len(apellido_solo)
    borrar_coma = posicion_coma -1
    apellido_nuevo = apellido_solo[0:borrar_coma]
    inicial = nombre_solo[0]
    inicial_c_p = inicial[0:] + "."
    

    print(inicial_c_p, apellido_nuevo)

#Listo

print("")
print("")
print("Proceso 2")
print("")
#   Nombre de pila mas largo.

c2 = -1
nombre_pila_largo = 0
nombre_largo = ""
for e in range(len(nombres)):
    c2 = c2 + 1
    nombre_de_pila = nombres[c2].split()
    nombre_de_pila = nombre_de_pila[1]
    cantidad_letra = len(nombre_de_pila)
    if cantidad_letra > nombre_pila_largo:
        nombre_pila_largo = cantidad_letra
        nombre_largo = nombre_de_pila


print("El nombre más largo es:  ", nombre_largo)
 
print("")

#Listo
print("")
print("Proceso 3")
print("")

#   Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)

fecha_hoy = "17/05/2023"

mujeres = []
c3 = -1
cantidad_mujeres = 0

for q in range(len(sexos)):
    c3 = c3 + 1
    if sexos[c3] == "f":
        cantidad_mujeres = cantidad_mujeres + 1


print(cantidad_mujeres)