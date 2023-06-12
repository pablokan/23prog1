# Mi programa principal en la aplicación Heladeria
""" import libreriaPablito # preserva los namespaces
edadCliente = libreriaPablito.inputInt("Ingrese la edad del cliente: ")
print(libreriaPablito.foo())
def foo():
    return "foo de main"
print(foo())
"""

#from libreriaPablito import * # trae TODAS las funciones de la libreria al namespace de main
from libs.libreriaPablito import inputInt, foo # importa funciones individuales
from libs.calculo_edad import edad


print(foo())
edadCliente = inputInt("Ingrese la edad del cliente: ")
print(foo())
print(edad("01/01/2000"))



