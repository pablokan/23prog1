lista = [1, 2, 3, 2, 4, 2, 5]
elementoAeliminar = int(input('Ingrese elemento a eliminar: '))
cO = len(lista)
print('Lista original:', lista)
while elementoAeliminar in lista:
    lista.remove(elementoAeliminar)
cA = len(lista)
if cO == cA:
    print(elementoAeliminar, 'no estaba')
else:
    print('Lista resultante:', lista)

