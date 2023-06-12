# Escribe una función que determine si dos listas tienen algún elemento en común.

def commonElement(l1, l2):
    for e1 in l1:
        if e1 in l2:
            return True
    return False

print(commonElement([1,2,3], [4,5,6]))

print(commonElement([1,2,3], [4,1,6]))