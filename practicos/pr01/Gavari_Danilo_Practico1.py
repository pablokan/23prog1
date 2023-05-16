#Proceso 1
datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/09/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
] 
 
lista = []
lista_apellidos = []
for i in datos:
   separar= i.split(",")
   nombre = separar [1:2] 
   apellido = separar [0:1]
   lista_apellidos.append(apellido) 
   lista.append(nombre)
   lista = separar [0]

print(lista, )
print(lista_apellidos)

