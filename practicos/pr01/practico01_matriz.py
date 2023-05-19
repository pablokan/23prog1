datos = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/09/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]

# En cambio, usaré el recorrido por elemento que es más claro
print('1)')
for persona in datos:
    nombre = persona[0]
    posComa = nombre.find(',')
    apellido = nombre[0:posComa]
    inicial = nombre[posComa + 2]
    print(inicial + '. ' + apellido)    

print('2)')
nombreMasLargo = ''
for persona in datos:
    nombre = persona[0]
    posComa = nombre.find(',')
    nombrePila = nombre[posComa + 2:]
    if len(nombrePila) > len(nombreMasLargo):
        nombreMasLargo = nombrePila        
print('El nombre más largo es', nombreMasLargo)

print('3)')
dH = 16
mH = 5
aH = 2023
cM = 0
acum = 0
for persona in datos:
    if persona[1] == 'f':
        cM += 1
        # Variante de obtención de día, mes y año con slicing
        dN = int(persona[2][:2])
        mN = int(persona[2][3:5])
        aN = int(persona[2][6:])
        
        edad = aH - aN
        if (mN > mH) or (mN == mH and dN > dH):
            edad -= 1
        acum += edad
print('El promedio de edad de las mujeres es:', acum//cM)





