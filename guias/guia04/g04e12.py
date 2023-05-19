frase = 'Juan tiene 25 años'
numero = ""

i = 0
while frase[i] not in "123456789":
    i += 1
print(int(frase[i] + frase[i+1])*2)


