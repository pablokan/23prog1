# def raya(caracter, cantidad):
#     for i in range(cantidad):
#         print(caracter, end='')
#     print()
def raya(caracter, cantidad):
    print(caracter * cantidad)

raya('-', 20)
raya('#', 30)

c = input('Ingrese un caracter: ')
q = int(input('Ingrese la longitud de la raya: '))
raya(c, q)

