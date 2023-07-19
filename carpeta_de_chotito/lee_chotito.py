# 4 formas de lectura

# 1. read()
with open('chotito.txt') as choty:
    print(choty.tell()) # posición de lectura
    todo = choty.read() # lee todo el archivo
    # y lo guarda como una string
    print(choty.tell()) 
    choty.seek(3) # mueve el puntero de lectura
    cuatroCars = choty.read(4) # lea 4 caracteres
    print(cuatroCars)
print(todo)

# 2. readline()
#with open('archivos/chotito.txt') as choty:
    
