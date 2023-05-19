ListaNombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio"
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

listaNombres = []
nombres = ["A","K", "B","S","C","A","W"]  
Apellidos = ["torres", "Hudson", "Quedesa","Campoamores","Santamaría","Skarsgard","Catalejos"] 
print(nombres)
print(Apellidos)

aH = 2023
mH = 5
dH = 17
aN = 1943
mN = 5
dN = 2

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1
print(edad)

aH = 2023
mH = 5
dH = 17
aN = 1984
mN = 9
dN = 7

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1

print(edad)
aH = 2023
mH = 5
dH = 17
aN = 1967
mN = 12
dN = 21

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1
print(edad)

aH = 2023
mH = 5
dH = 17
aN = 1995
mN = 8
dN = 30

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1
print(edad)     
mujeres=['Ana','kate','Susana','Azul']
edades=[80, 38, 55,27]
print(mujeres,edades)