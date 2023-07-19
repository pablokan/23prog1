with open('choto.txt', 'w') as a:
    a.write('quico\njuan')

lista1 = ['linea 1\n', 'linea 2\n']
with open('choto.txt', 'w') as a:
    a.writelines(lista1)

lista2 = ['linea 3\n', 'linea 4\n']
with open('choto.txt', 'a') as a:
    a.writelines(lista2)


