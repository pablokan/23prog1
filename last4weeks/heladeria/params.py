def saludo(nombre, edad=100): # edad es un parámetro con un valor por defecto
    print("Hola", nombre, "tenés", edad, "años")

saludo("Ana", 44)
saludo("Pipo") # vale 100, el valor por defecto al no mandarle nada en edad

def suma(*args): # args es una tupla
    print(args)
    t = 0
    for x in range(len(args)):
        t += args[x]
    return t

print(suma(1,2))
print(suma(1,2,6,7))
print(suma())

def foo(p1, p2, *args, n1="<uno>", n2="<dos>"): # orden obligatorio: posicionales, args, nominados y diccionario
    print(p1, p2, args, n1, n2)

foo(1, 2, 3, 4, 5, n2="<nuevo valor de n2>")



