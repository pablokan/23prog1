datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/09/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]
nombres = ""
for i in range(len(datos)):
    n = datos[i].split(",")
    nombres = (nombres + n[1][:2] + "." + " "+ n[0])
print(nombres)

nMasLargo = []
for t in range(len(datos)):
    l = datos[t].split(",")
    nML = l[1]
    nMasLargo.append(nML)
print(nMasLargo[2])

cantMujeres = 0
for p in range((len(datos))):
    r = datos[p].split(",")
    s = r[2]
    for t in range(len(s)):    
        if s == "f":
            cantMujeres = cantMujeres + 1
print(cantMujeres)