# 2 modos de escritura

# Modo 1: write()
# 'w' arranca de cero, si no existe lo crea
# si existe lo pisa
with open('archivos/beltran.txt', 'w') as bel:
    bel.write('fdskj;sfjdg')

# 'a' agrega al final del archivo
with open('archivos/beltran.txt', 'a') as bel:
    bel.write('\nagregado con a')

with open('archivos/beltran.txt', 'w') as bel:
    bel.write('pisa todo')

# Modo 2. writelines()
lista = ['juan\n', 'anita\n']
with open('archivos/beltran.txt', 'w') as bel:
    bel.writelines(lista)
    


