# Trabajo practico 1- Velazquez Alejo

datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/09/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]

#  Proceso 1: Mostrar las iniciales de los nombres con un punto,
# luego un espacio y finalmente el apellido completo de todas las personas.
name_max = ''
lista_nombres = []
print('1) Iniciales y apellido de las personas: ')
for element in datos:
   list = element.split(',') 
   for i in range (len(list)): # Utilizo el len(list) para trabajar con las posiciones de la lista individuamente, a diferencia de ciclar por elemento
      if i == 1: # Viendo los datos, en la posicion 1 se encuentran lus nombres, por lo que limitaremos al if para que trabaje solo con esa posicion de la lista. Este es un proceso para la siguiente actividad
         lista_nombres.append(list[i]) # Creo una lista con todos los nombres de la lista, asi sera mas facil trabajar en la siguiente actividad.
   dato = list[1][1] + '.' + ' ' + list[0] # Creo una variable para que sea mas facil su modificacion de hacer falta, y que no printee en cada ciclo
   print(dato)

print(' ')

# Proceso 2: Decir cuál es el nombre de pila más largo
for element in lista_nombres: # Utilizando la lista de nombres anteriormente creada, solo tendremos en cuenta calcular la cantidad de caracteres que hay en cada termino, siendo el de mayor termino el nombre mas largo
   if len(name_max) < len(element):
      name_max = element    
print('2) El nombre de la lista mas largo es:', name_max)

print(' ')

# Proceso 3: Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py
# que está subido en el Classroom)
contador = 0
edad_total = 0
for element in datos:
   if element.find('f') != -1: # Con este find limito el if para que solo trabaje con el termino de la lista que posee rl sexo femenino ('f')
      list = element.split(',')
      list = list[len(list) - 1].split('/') # Separo en terminos cada uno de los valores de la fecha que representan el dia, el mes y el año
      contador = contador + 1 # Guardo la cantidad de mujeres
      edad_total = edad_total + 2023 - int(list[len(list) - 1]) # Sumo todas las edades, que consigo al restarle el año de nacimiento al año actual, y los guardo para que queden en el siguiente ciclo
      if int(list[1]) > 5:
          edad_total = edad_total - 1
      elif int(list[0]) > 15: # Este paso es para filtrar la edades falsas, mujeres que no han cumplido años aun, y anteriormente no se tuvo en cuenta. Se verifica que el dia sea mayor al dia de hoy o no, al igual que el mes.
        edad_total = edad_total - 1
edad_prom = edad_total // contador
print('3) El promedio de edad de las mujeres es:', edad_prom)
