# Implementa una función que determine si una cadena de texto contiene solo caracteres numéricos 
# (es decir, si es un entero).

def isInteger(s):
    for d in s:
        if d not in '1234567890':
            return False
    return True

print(isInteger('67686'))
print(isInteger('67q686'))
print(isInteger('hola'))



