palabra = 'español'
palabraEnMayusculas = ''
for letra in palabra:
    palabraEnMayusculas += chr(ord(letra) - 32)

print(palabraEnMayusculas)

