# 3_460_000 12_850_000
precio = 1
c = 0
while precio != 0:
    auto = input('Auto: ')
    precio = int(input('Precio: '))
    #if  3_460_000 < precio < 12_850_000:
    if  precio > 3_460_000 and precio < 12_850_000:
        c = c + 1
print('La cantidad de autos cuyo precio está entre $3.460.000 y $12.850.000 es', c)
