data = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/09/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]

print("1) Iniciales y apellido de las personas:")
for info in data:
    nameSplited = info[0].split(',')
    name = nameSplited[0]
    lastName = nameSplited[1]

    print(f"{name[0]}.{lastName}")


largestName = ''
for i in range(len(data)):
    nameSplited = data[i][0].split(',')
    name = nameSplited[0]
    if len(name) > len(largestName):
        largestName = name

print("")
print(f"2) El nombre más largo es: {largestName}")


aH = 2023
mH = 5
dH = 17

womenQuantity = 0
womenAge = 0

for info in data:
    if info[1] == 'f':
        womenQuantity += 1

        ageSplit = info[2].split('/')

        age = aH - int(ageSplit[2])
        if (int(ageSplit[1]) > mH) or (int(ageSplit[1]) == mH and int(ageSplit[0]) > dH):
            age -= 1

        womenAge += age

averageWomenAge = womenAge / womenQuantity
print("")
print(f"3) El promedio de edad de las mujeres es: {averageWomenAge}")