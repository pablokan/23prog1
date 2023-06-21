def carga():
    nombres = []
    for i in range(3):
        nombre = input('Nombre: ')
        nombres.append(nombre)
    return nombres

listaNombres = carga() # la función vale lo que vuelve en el return

def posNombre(lista, nombre):
    for i in range(len(lista)):
        if lista[i] == nombre:
            return i
    return -1

nn = input('Nombre a buscar: ')
posi = posNombre(listaNombres, nn)
if  posi == -1:
    print('no ta')
else:
    print('está en la posición', posi )
    
