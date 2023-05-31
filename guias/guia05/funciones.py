def funcioncita(): # declaración de la función
    print('esta string está dentro de funcioncita')

def otraFuncion():
    return 'frase retornada'

def saludo(nombre, edad): # nombre y edad son parámetros posicionales obligatorios
    print('Hola', nombre, 'tenés', edad, 'años')

# Programa Principal
print('Inicio de ejecución del programa')

funcioncita() # llamada == call == ejecución

valorDevuelto = otraFuncion() # devuelve en si misma el valor de retorno
print(valorDevuelto)

saludo('Pipo', 11) # los argumentos deben ser mismo tipo, cantidad y orden
n = input('Ingrese su nombre: ')
e = int(input('Ingrese su edad: '))
saludo(n, e) # NO el mismo nombre de los parámetros

print('Fin del programa')


