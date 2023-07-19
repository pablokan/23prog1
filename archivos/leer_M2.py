# 4 modos de lectura
""" 
# Modo 1: read()
with open('archivos/riquelme.txt') as archi:
    print(archi.tell()) # muestra posición de lectura
    todo= archi.read() # lee todo y guarda en una string
    print(archi.tell()) 
    archi.seek(4) # mueve la posición de lectura
    tresCaracteres = archi.read(3) # lee 3 bytes
    print(tresCaracteres)
print(todo)
 
# Modo 2: readline()
with open('archivos/riquelme.txt') as archi:
    linea = archi.readline()
    print(linea)


# Modo 3: readlines()
with open('archivos/riquelme.txt') as archi:
    lineas = archi.readlines()
    print(lineas)    
"""

# Modo 4: recorrido con for
with open('archivos/riquelme.txt') as archi:
    for linea in archi:
        print(linea, end='')
