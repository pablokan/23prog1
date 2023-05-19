hayMas = 's'
cantidadVocales = 0
listaLetras = []
while hayMas == 's':
    letra = input('Ingrese una letra: ')
    listaLetras.append(letra)
    hayMas = input('Más letras? (s/n)? ')

for letra in listaLetras:
    if letra in 'aeiou':
        cantidadVocales += 1

print('La cantidad de vocales es', cantidadVocales)
