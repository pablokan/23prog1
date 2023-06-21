# Implemente una función que calcule el promedio de una cantidad variable de números. Se tiene que poder pasar un argumento que descarte los valores negativos para sacar dicho promedio.

def promedio(*args, sinNegativos=False):
    acumPositivos = 0
    cantPositivos = 0
    acumTodos = 0
    for n in args:
        if sinNegativos and n >= 0:
            acumPositivos += n
            cantPositivos += 1
        acumTodos += n
    if sinNegativos:
        return acumPositivos / cantPositivos
    else:
        return acumTodos / len(args)
    
print(promedio(121,65,-88,34,-9,27)) # 150/6=25
print(promedio(121,65,-88,34,-9,27, sinNegativos=True)) #247/4=61.75
