datos = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/09/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]
aH = 2023
mH = 5
dH = 15
max=0
cont=0
sumatoria=0
print("1) Iniciales y apellido de las personas: ")
for dato in datos:
    #resolucion ejercicio 1
    inicial=dato[0].split(",")
    print(inicial[1][1]+".",inicial[0])
    #resolucion ejercicio 2
    longitud=len(inicial[1])
    if longitud>max:
        max=longitud
        masLargo=inicial[1]
    #resolucion ejercicio 3
    if dato[1]=="f":
        aN=int(dato[2][6:])
        mN=int(dato[2][3:5])
        dN=int(dato[2][:2])
        edad = aH - aN
        if (mN > mH) or ((mN == mH) and (dN > dH)):
            edad -= 1
        sumatoria+=edad
        cont+=1
        
promedio=sumatoria/cont

print("2) El nombre más largo es:",masLargo)

print ("3) El promedio de edad de las mujeres es:",promedio)