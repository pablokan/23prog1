""" with open('pepito.txt') as archy:
    print(archy.tell())
    todo = archy.read()
    print(archy.tell())
    archy.seek(5)
    tresBytes = archy.read(3)
    print(tresBytes)
print(todo) 


with open('pepito.txt') as archy:
    print(archy.readline())


with open('pepito.txt') as archy:
    lineas = archy.readlines()
    print(lineas)
"""

with open('pepito.txt', 'r') as archy:
    for linea in archy:
        print(linea, end='')
