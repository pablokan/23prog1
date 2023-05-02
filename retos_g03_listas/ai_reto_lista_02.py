def contar_bumeranes(lista):
    contador = 0
    for i in range(len(lista)-2):
        if lista[i] == lista[i+2] and lista[i] != lista[i+1]:
            print("Búmeran encontrado:", lista[i], lista[i+1], lista[i+2])
            contador += 1
    print("Número total de bumeranes:", contador)

# Lista de prueba
lista = [1, 2, 3, 2, 1, 5, 6, 7, 8, 8, 9, 8, 8, 7, 5, 4]

# Llamamos a la función para contar los bumeranes y mostrarlos
contar_bumeranes(lista)
