s = 'Juan$120000,Ana$250000,Luis$76500,Vilma$98700'
nombres = []
sueldos = []

personas = s.split(',')
for persona in personas:
    p = persona.split('$')
    nombres.append(p[0])
    sueldos.append(int(p[1]))

print(nombres, sueldos)
