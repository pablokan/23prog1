def insertarContenido(filename, posicion, contenido):
    with open(filename, 'r') as file:
        data = file.read()
    nueva_data = data[:posicion] + contenido + data[posicion:]
    with open(filename, 'w') as file:
        file.write(nueva_data)

insertarContenido('archivos/qqq.txt', 6, 'chau')

def insertarFila(filename, fila, contenido):
    with open(filename, 'r') as file:
        data = file.readlines()
        contenido += '\n'
        data.insert(fila-1, contenido)
    with open(filename, 'w') as file:
        file.writelines(data)

insertarFila('archivos/qqq.txt', 2, 'fila nueva')
