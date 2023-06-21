# Pedir dos números enteros, validarlos y sumarlos

def inputInt(mensaje):
    validado = False
    while not validado:
        try:
            n = int(input(mensaje))
            validado = True
        except:
            print('no es entero, intente de nuevo!')
    return n

entero1 = inputInt('Ingrese el primer número: ')
entero2 = inputInt('Ingrese el segundo número: ')
print('La suma es', entero1 + entero2)





