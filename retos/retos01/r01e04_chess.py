fila = 2
columna = 9
if 0<= fila <= 7 and 0<= columna <= 7:
    if (fila + columna) % 2 == 0:
        print('blanca')
    else:
        print('negra')
else:
    print('afuera')


