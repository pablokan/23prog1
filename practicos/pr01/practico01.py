nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 
sexos = ["f","f","m","f","m","f","m"]
fechas = [
"02/05/1943",
"07/09/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]

# Solución para un elemento individual con find
""" 
nombre = "Catalejos, Walter"
posComa = nombre.find(',')
apellido = nombre[0:posComa]
inicial = nombre[posComa + 2]
print(inicial + '. ' + apellido)
"""

# Variante con split
""" 
nombre = "Skarsgard, Azul"
apellidoYnombre = nombre.split(', ') # ['Skarsgard', 'Azul']
inicial = apellidoYnombre[1][0]
apellido = apellidoYnombre[0]
print(inicial + '. ' + apellido)
"""

# NO voy a usar el recorrido por índice porque no necesito saber las posiciones
""" 
for i in range(len(nombres)):
    print(nombres[i])
"""

# En cambio, usaré el recorrido por elemento que es más claro
print('1)')
for nombre in nombres:
    posComa = nombre.find(',')
    apellido = nombre[0:posComa]
    inicial = nombre[posComa + 2]
    print(inicial + '. ' + apellido)    

print('2)')
nombreMasLargo = ''
for nombre in nombres:
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
for i in range(len(sexos)):
    if sexos[i] == 'f':
        cM += 1
        # Variante de obtención de día, mes y año con slicing
        # dN = int(fechas[i][:2])
        # mN = int(fechas[i][3:5])
        # aN = int(fechas[i][6:])
        
        # Variante con split
        dN, mN, aN = fechas[i].split('/')
        dN, mN, aN = int(dN), int(mN), int(aN)

        edad = aH - aN
        if (mN > mH) or (mN == mH and dN > dH):
            edad -= 1
        acum += edad
print('El promedio de edad de las mujeres es:', acum//cM)





