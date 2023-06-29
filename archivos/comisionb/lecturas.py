# 4 modos de lectura

# 1. read()
with open('pepito.txt') as archy:
    print(archy.tell()) # muestra la posición del puntero
    todo = archy.read() # read() sin argumentos lee todo el archivo
    print(archy.tell()) 
    archy.seek(5) # posiciona el puntero
    tresBytes = archy.read(3) # lee 3 bytes
    print(tresBytes)
print(todo) 

# 2. readline()
with open('pepito.txt') as archy:
    print(archy.readline()) # lee una línea entera

# 3. readlines()
with open('pepito.txt') as archy:
    # lee todo el archivo y lo guarda en una lista
    lineas = archy.readlines() 
    print(lineas)

# 4. recorrido con for
with open('pepito.txt', 'r') as archy:
    for linea in archy:
        print(linea, end='')
