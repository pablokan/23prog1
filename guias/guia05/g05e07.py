#Almacenar en dos  listas paralelas, nombres y sexos de 8 personas.
#Al finalizar, recorrerlas y mostrar los nombres de las mujeres. Dos funciones: carga y mostrarMujeres
def carga():
    nombres = []
    sexos = []
    for datos in range(3):
        nombre = input("ingrese nombre: ")
        nombres.append(nombre)
        sexo = input("ingrese sexo (f/m): ")
        sexos.append(sexo)
    return nombres, sexos

def mostrarMujeres(nombres, sexos):
    femenino = []
    for i in range (len(sexos)):
        if sexos[i] == "f":
            femenino.append(nombres[i])
    return femenino

print(mostrarMujeres(*carga()))
