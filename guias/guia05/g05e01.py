frase = 'Quiero comer manzanas, solamente manzanas.'
letrita = 'a'

def contarLetra(letra, cadena):
    c = 0
    for caracter in cadena:
        if letra == caracter:
            c += 1
    return c
    
print('La cantidad de veces que aparece la letra', letrita, 'en', frase, 'es', contarLetra(letrita, frase))

print(contarLetra('s', 'masomenos'))

f = input('Frase: ')
l = input('Letra: ')
print(contarLetra(l, f))
