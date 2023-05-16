mujeres = ['Lisa', 'Ema', 'Juana', 'Ester']
varones = ['Eduardo', 'Pedro']
inicial = 'E'

salida = ''
for persona in mujeres:
    if inicial == persona[0]:
        salida += persona + "-"

for persona in varones:
    if inicial == persona[0]:
        salida += persona + "-"

print(salida[:-1])