datos = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/09/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]

# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio
# y finalmente el apellido completo de todas las personas.

for persona in datos:
    nombre_y_apellido = persona[0].split(", ")
    nombre = nombre_y_apellido[1]
    apellido = nombre_y_apellido[0]
    inicial_del_nombre = nombre[0]
    print(inicial_del_nombre, ".", apellido)