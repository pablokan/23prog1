from devtools import debug


frase = 'Yo soy oso, el amo del radar y del ojo.'
# Eliminar puntuación
fraseLimpia = ''
for caracter in frase:
    if caracter not in ',.':
        fraseLimpia += caracter
print(fraseLimpia)
lista = fraseLimpia.split()
palindromos = []
for palabra in lista:
    if palabra == palabra[::-1]:
        palindromos.append(palabra)
print(frase, palindromos)
