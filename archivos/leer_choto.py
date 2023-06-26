with open('choto.txt') as archivo:
    print(archivo.tell()) # mostrar posición
    todo = archivo.read() # lectura total
    print(archivo.tell())
    archivo.seek(9) # posicionar
    print(archivo.read(4)) # leer 4 caracteres
print(todo)

with open('choto.txt') as archivo:
    lineas = archivo.readlines() # lee todo y guarda en una lista, cada línea en una string
print(lineas)

with open('choto.txt') as archivo:
    # con for se hace lectura directa por línea
    for linea in archivo:
        print(linea)

with open('choto.txt') as archivo:
    finArchivo = False
    while not finArchivo:
        l = archivo.readline() # lectura de una sola línea
        if l != '':
            print(l, end='')
        else:
            finArchivo = True

