lista = ['quico', 123, 'mesa']
separador = '<->'
cadena = ''
ultimo = len(lista)-1
for i in range(ultimo):
    cadena += str(lista[i]) + separador
cadena += lista[ultimo]
print(cadena)
