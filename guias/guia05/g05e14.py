# Crea una función que calcule la suma de los dígitos de un número entero.

def sumDigits(n):
    t = 0
    n = str(n)
    for d in n:
        d = int(d)
        t += d
    return t

print(sumDigits(123))
print(sumDigits(842))