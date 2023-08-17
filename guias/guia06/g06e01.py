def concatenar(*args, conector=' '):
    cadena = ''
    for s in args:
        cadena += s + conector
    cadena = cadena[:-(len(conector))]
    return cadena

print(concatenar('hola', 'pibe'))
print(concatenar('hola', 'pibe', conector='@'))
print(concatenar('techo', 'mesa', 'árbol', conector='###'))
print(concatenar('techo', 'mesa', 'árbol', conector='|||||||'))

    