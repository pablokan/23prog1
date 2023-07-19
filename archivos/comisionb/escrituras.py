# 2 modos de escritura

# 1. write()
with open('montoto.txt', 'w') as monty: # la 'w' es el modo de apertura
    monty.write('josé manuel morete\notra cosa')

with open('montoto.txt', 'a') as monty:
    monty.write('\ntercera línea')

# 2. writelines()
lista = ['\nfila1', '\nfila2']
with open('montoto.txt', 'a') as monty:
    monty.writelines(lista) # escribe todos los elementos de la lista
