from funks import inputInt

def inputChoice(options, msg='Ingrese opción: '):
    optionsList = options.split('/') 
    ch = 0
    while not 1 <= ch <= len(optionsList):
        for i, v in enumerate(optionsList, start=1):
            print(i, v)
        ch = inputInt(msg, 'no es una opción válida')
    return optionsList[ch-1]

print(inputChoice('verde/rojo/azul/blanco', 'Elija un color: '))
