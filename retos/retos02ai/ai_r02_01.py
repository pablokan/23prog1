# Función que comprueba si la lista está ordenada ascendentemente y sin elementos repetidos
def comprobar_lista(lista):
    for i in range(len(lista)-1):
        if lista[i] >= lista[i+1]:
            return False
    return True

# Función que genera una nueva lista con los elementos faltantes
def generar_nueva_lista(lista):
    nueva_lista = []
    for i in range(lista[0], lista[-1]+1):
        if i not in lista:
            nueva_lista.append(i)
    return nueva_lista

# Lista de prueba
lista = [1, 2, 3, 5, 8, 9, 10]

# Comprobamos si la lista cumple con las condiciones iniciales
if not comprobar_lista(lista):
    print("La lista no está ordenada ascendentemente o tiene elementos repetidos")
else:
    # Generamos la nueva lista
    nueva_lista = generar_nueva_lista(lista)

    # Mostramos ambas listas
    print("Lista original:", lista)
    print("Nueva lista:", nueva_lista)
