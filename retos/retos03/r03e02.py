mujeres = ['Lisa', 'Ema', 'Juana', 'Ester']
varones = ['Eduardo', 'Pedro']
inicial = 'E'

salida = ''
personas = mujeres + varones
for persona in personas:
    if persona[0] == inicial:
        salida = salida + persona + '-'
salida = salida[:-1]
print(salida)
