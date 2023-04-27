# Dada una lista de enteros
# Obtener el promedio
# Y mostrar los valores de la lista
# que son mayores que dicho promedio
# Ej:
# [1,2,3,4,5] total=15, promedio 3
# y los valores mayores son 4 y 5

# Carga de números [123, 1, 300, 65, 89]
numeros = []
hayMas = 'si'
while hayMas == 'si':
    n = int(input('Ingrese un número: '))
    numeros.append(n)
    hayMas = input('Hay más? (si/no): ')

# Proceso de obtención del promedio
cantidad = len(numeros)
total = 0
for i in range(cantidad):
    total = total + numeros[i]
promedio = total / cantidad
print(numeros, promedio)

# Proceso para obtener los valores mayores
# al promedio
for numero in numeros:
    if numero > promedio:
        print(numero)

