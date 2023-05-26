from devtools import debug


cadena = 'Pedro$120.000, Ana(frontend)$512.700, el portero$175.120, el pibe del backend(capaz hay que actualizarle!)$371.459, revisar bien el total de erogaciones!'

personas = cadena.split(',')
personas.pop()
total = 0
for persona in personas:
    posPesos = persona.find('$')
    salario = persona[posPesos+1:]
    salarioSinPunto = ''
    for caracter in salario:
        if caracter != '.':
            salarioSinPunto += caracter
    total += int(salarioSinPunto)
print('El total de salarios es', total)
