d = {"uno": "one", "dos": 2, "uno": "otro one"} # la clave es única
print(d["dos"])
print(d) # se eliminó el primer elemento

d["tres"] = "three" # se agrega por asignación
print(d)

del d["uno"] # elimina
print(d)
v = d.pop("dos") # elimina de la lista pero asigna el valor
print(d, v)

otroDic = {"a": 1, "b": 2, "c": 3}

print("Solamente las claves")
for k in otroDic.keys(): # da igual poner solo el nombre del dict
    print(k)

print("Solamente los valores")
for v in otroDic.values():
    print(v)

for k, v in otroDic.items():
    print(f"Clave: {k} ---> Valor: {v}")

# Diccionario en modo homogéneo
# pares clave-valor similares e independientes
remeras = {"rojas": 3, "verdes": 12, "azules": 1}
remeras["amarillas"] = 22
# Diccionarios tipo registro
# pares clave-valor con elementos dependientes y distintos
persona = {"nombre": "Juan", "edad": 22}

personas = [
    {"nombre": "Juan", "edad": 22},
    {"nombre": "Pedro", "edad": 32},
    {"nombre": "Ana", "edad": 52}
]

for persona in personas:
    print(persona['nombre'], persona['edad'])

for persona in personas:
    if persona['nombre'] == 'Ana':
        print(persona["edad"])

