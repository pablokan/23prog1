cadena = 'Juan$120000,Ana$250000,Luis$76500,Vilma$98700'

personas = cadena.split(',')
nombres = []
salarios = []
for persona in personas: 
    posSignoPesos = persona.find('$')
    nombre = persona[:posSignoPesos]
    salario = persona[posSignoPesos+1:]
    nombres.append(nombre)
    salarios.append(int(salario))
print(nombres, salarios)

