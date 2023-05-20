cadena = 'Juan$120000,Ana$250000,Luis$76500,Vilma$98700'
nombres = []
sueldos = []
lista = cadena.split(',')
for persona in lista:
    nombre, sueldo = persona.split('$')
    nombres.append(nombre)
    sueldos.append(int(sueldo))

print(nombres, sueldos)
