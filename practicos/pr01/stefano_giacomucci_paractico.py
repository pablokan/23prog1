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
for i in range(7):#punto 1
    nombres[i].split(",")
    aux = nombres[i]
    nombres[i] = nombres[len(nombres)-1-i]
    nombres[len(nombres)-1-i] = aux
    print(nombres[i])

#for x in range(7):
    #nombres[x].split(",")
    #aux = nombres[i]
    #nombres[i] = nombres[len(nombres)-1-i]
    #nombres[len(nombres)-1-i] = aux
    

#for i in range(7):#punto 3
    #if sexos[i]=="f":
        #print((fechas[i].split("/")))
        #aH = 23
        #mH = 5
        #dH = 3
        #aN = int(fechas[i])
        #mN = int(fechas[i])
        #dN = int(fechas[i])

        #edad = aH - aN
        #if (mN > mH) or ((mN == mH) and (dN > dH)):
            #edad -= 1