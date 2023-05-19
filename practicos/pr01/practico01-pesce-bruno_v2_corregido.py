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

#Ciclo para sacar la inicial de cada nombre

for name in nombres:
    last_n, name = name.split(", ")
    ini = name[0]
    # Convenía concatenar para que no pusiera el espacio luego de la inicial
    print(ini,".",last_n)


#Ciclo para buscar el nombre mas largo

name_longer = ""

for name1 in nombres:
    last_n1, name1 = name1.split(", ")
    if len(name1) > len(name_longer):
        name_longer = name1

print ("El nombre mas largo es:",name_longer)


#Ciclo para sacar el promedio de las mujeres

#Cantidad mujeres

aH = 2023
mH = 5
dH = 17
womans = 0
age = 0

# No hace falta contar acá
for sex in sexos:
        if sex == "f":
                womans = womans + 1

#Edad de las mujeres

e = 0    
# Aquí era más razonable el recorrido por indice           
for age1 in fechas:
        if sexos[e] == "f":
                # Se podía contar acá
                day, month, year = age1.split("/")
                aN = int(year)
                mN = int(month)
                dN = int(day)
                age_aux = aH - aN
                if (mN > mH) or ((mN == mH) and (dN > dH)):
                        age_aux -= 1
                age = age + age_aux
        e = e+1

print("El promedio de edad de las mujeres es: ",age/womans,"años.")
                         

    


