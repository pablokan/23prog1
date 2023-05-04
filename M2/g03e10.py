dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
diaMasLluvioso = ''
mayorCantidadMM = 0
t = 0
for x in range(7):
    print(dias[x])
    mm = int(input('Lluvia caída en mm: '))
    t += mm
    if mm > mayorCantidadMM:
        mayorCantidadMM = mm
        diaMasLluvioso = dias[x]
print('El total de lluvia caída es', t)
print('El día que más llovió fue el', diaMasLluvioso)

