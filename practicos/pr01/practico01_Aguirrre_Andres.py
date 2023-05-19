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


nombre = ["Ana", "Kate", "Benicio", "Susana"," Carlos"," Azul", "Walter"]
apellido = ["Torres","Hudson","Quesada","Campoamores","Santamaria","SKargard","Catalejos"]

cont = 0 

lista = []

for i in range(len(nombre)):
    cont = cont + 1 
    lista.append(nombre[i] + "." + apellido[i])

for i in range(len(lista)): 
    print(lista[i])

print("nombre mas largo: ",nombre[2])

aH = 2023
mH = 5
dH = 3
aN = 1943
mN = 5
dN = 2

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1

print(edad)

aH = 2023
mH = 5
dH = 7
aN = 1984
mN = 9
dN = 7

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1

print(edad)

aH = 2023
mH = 7
dH = 13
aN = 1967
mN = 12
dN = 21

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1

print(edad)

aH = 2023
mH = 5
dH = 3
aN = 1995
mN = 8
dN = 31

edad = aH - aN
if (mN > mH) or ((mN == mH) and (dN > dH)):
    edad -= 1

print(edad)
mujeres= ['Ana','Kate','Susana','Azul']
edad= [80,38,55,27]
print(mujeres,edad)