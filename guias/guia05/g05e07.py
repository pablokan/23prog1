#Almacenar en dos  listas paralelas, nombres y sexos de 8 personas.
#Al finalizar, recorrerlas y mostrar los nombres de las mujeres. Dos funciones: carga y mostrarMujeres
nombres = []
sexos = []
def carga(nombre, sexo):
    for datos in range(3):
        nombre = input("ingrese nombre: ")
        nombres.append(nombre)
        sexo = input("ingrese sexo (F/M): ")
        sexos.append(sexo)

def mostrarMujeres():
    femenino = []
    for i in range (len(sexos)):
        if sexos[i] == "f":
            femenino.append(nombres[i])
    return femenino

carga(nombres, sexos)
print(mostrarMujeres())