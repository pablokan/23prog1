hayDatos = input('hay datos para ingresar? (si/no): ')
while hayDatos == 'si':
    num = int(input('Ingrese un entero: '))
    if num < 0:
        print('es negativo')
    else:
        print('no es negativo')
    hayDatos = input('quiere repetir? (si/no): ')
print('fin del programa')

