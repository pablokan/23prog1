# Hacer una función que determine si una cadena de texto contiene todas las vocales.

def allVowels(s):
    for v in 'aeiou':
        if v not in s:
            return False
    return True

print(allVowels('murcielago'))
print(allVowels('murcia'))
print(allVowels('elena'))


