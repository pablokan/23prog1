personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]
nombres = []
continentes = []
fechas = []
for persona in personas:
    posEspacio = persona.find(' ')
    nombre = persona[:posEspacio]
    nombres.append(nombre)
    posParentesis = persona.find('(')
    continente = persona[posParentesis+1: -12]
    continentes.append(continente)
    anio = int(persona[-4:])
    fechas.append(anio)

aM = 0
chaboncito = ''
for i in range(len(continentes)):
    if continentes[i] == 'Europe':
        if fechas[i] > aM:
            aM = fechas[i]
            chaboncito = nombres[i]

print(chaboncito)


