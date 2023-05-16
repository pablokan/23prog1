frase = 'Quiero comer manzanas, solamente manzanas, puras manzanas dije!'
palabraVieja = 'manzanas'
palabraNueva = 'peras'

while palabraVieja in frase:
    posVieja = frase.find(palabraVieja)
    inicio = frase[:posVieja]
    final = frase[posVieja+len(palabraVieja):]
    frase = inicio + palabraNueva + final

print(frase)
