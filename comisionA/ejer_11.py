#Cargar en listas los nombres y fechas de nacimiento de varias personas, 
#luego recorrerlo y mostrar los nombres de los mayores de edad. 
# Funciones de carga y cálculo de edad.
def nombres():
    nombres = []
    for i in range(3):
        nombre = input("Ingrese el nombre: ")
        fecha = input("Ingrese la fecha de nacimiento (en formato dd.mm.aaaa): ")
        nombres.append((nombre, fecha))
    return nombres

def calcularEdad(fechaNacimiento, fechaActual):
    diaNac, mesNac, anioNac = fechaNacimiento.split('.')
    diaAct, mesAct, anioAct = fechaActual.split('.')

    edad = int(anioAct) - int(anioNac)

    if int(mesAct) < int(mesNac):
        edad -= 1
    elif int(mesAct) == int(mesNac) and int(diaAct) < int(diaNac):
        edad -= 1

    return edad

datos = nombres()
fechaActual = input("Ingrese la fecha actual (en formato dd.mm.aaaa): ")

for nombre, fechaNacimiento in datos:
    edad = calcularEdad(fechaNacimiento, fechaActual)
    print("Nombre:", nombre)
    #print("Fecha de Nacimiento:", fechaNacimiento)
    print("Edad:", edad, "años")
    print()
           
    
