def contarLetra(letra, cadena):
    c = 0 # variable local (solamente existe aquí dentro)
    for elemento in cadena:
        if elemento == letra:
            c += 1
    return c

t = "Quiero comer manzanas, solamente manzanas."
l = 'e'
print('La cantidad de veces que está la letra', l, 'en', t, 'es:')
print(contarLetra(l, t))
print(contarLetra('q', 'riquelme'))
# print(c) Esto no se puede hacer por la variable c solo existe dentro de la función







