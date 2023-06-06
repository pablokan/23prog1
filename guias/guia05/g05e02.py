f = "Quiero comer manzanas, solamente manzanas."
pV = "manzanas"
pN = "peras"

def reemplazarPalabra(palabraVieja, palabraNueva, frase):
    while palabraVieja in frase:
        posicionPalabraVieja = frase.find(palabraVieja)
        inicio = frase[:posicionPalabraVieja]
        final = frase[posicionPalabraVieja+len(palabraVieja):]
        frase = inicio + palabraNueva + final
    return frase

print(reemplazarPalabra(pV, pN, f))




