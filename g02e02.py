hayDatos = input('hay datos para ingresar? (si/no): ')
while hayDatos == 'si':
    numEntero = int(input('Ingresar un entero: '))
    if numEntero < 0:
        print('es negativo')
    else:
        print('no es negativo')
    hayDatos = input('Quiere repetir? (si/no): ')

print('fin del programa')
