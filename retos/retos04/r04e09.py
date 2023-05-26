# paréntesis

cadena = 'hola (dj((djdjdjd , );s;() ) djdjd dsjkds  kfsjkf.) djskf.'

p = 0
for c in cadena:
    if c == "(":
        p += 1
    elif c == ')':
        p -= 1
    if p < 0:
        print('Error. Hay un paréntesis de cierre mal ubicado')
        break
if p == 0:
    print('Los paréntesis están correctamente emparejados')
elif p > 0:
    print('No están emparejados, faltan cierres')
