hayMas = 'si'
maximo = 0
while hayMas == 'si':
    numero = int(input('Ingrese un valor: '))
    if numero > maximo:
        maximo = numero
    hayMas = input('Hay mas? (si/no): ')    
print('El número ingresado más grande es', maximo)
