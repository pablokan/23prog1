names = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana", 
    "Santamaría, Carlos",
    "Skarsgard, Azul", 
    "Catalejos, Walter"
] 
sexs = ["f","f","m","f","m","f","m"]
dates = [
    "02/05/1943",
    "07/09/1984",
    "10/02/1971",
    "21/12/1967",
    "30/01/1982",
    "30/08/1995",
    "18/07/1959"
]

# Ejercicio 1
printNames = []
print('Iniciales y apellido de las personas: ')
for name in names:
    aux = name.split(',')
    firstName = aux[1]
    lastName = aux[0]
    output = firstName[1] + '. ' + lastName
    printNames.append(output)
    print(output)

# Ejercicio 2
print('\n')
print('El nombre mas largo es: ')
firstNames = []
for name in names:
    aux = name.split(',')
    firstNames.append(aux[1])

longerName = ''
for firstName in firstNames:
    if len(firstName) > len(longerName):
        longerName = firstName
print(longerName)

# Ejercicio 3
print('\n')
print('El promedio de edad de las mujeres es: ')
womenBirthdays = []
for i in range(len(sexs)):
    if sexs[i] == 'f':
        womenBirthdays.append(dates[i])

dateNow = ["17", "05", "2023"]
averageAge = 0
count = 0
for birthday in womenBirthdays:
    date = birthday.split('/')
    age = int(dateNow[2]) - int(date[2])
    if (int(date[1]) > int(dateNow[1])) or ((int(date[1]) == int(dateNow[1])) and (int(date[0]) > int(dateNow[0]))):
        age -= 1

    averageAge += age
    count += 1

print(averageAge / count)





