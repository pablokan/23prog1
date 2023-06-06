# Buscar una palabra y reemplazarla por otra todas las veces que aparezca. 
#Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'

def buscador(cadena,busca):
    remplaza = input("ingrese palabra nueva: ")
    cadena_nueva = ""
    cadena = c.split(" ")
    for palabra in cadena:
        if busca in palabra:
            nueva = remplaza
            cadena_nueva +=" "+nueva 
        else:
            nueva = palabra
            cadena_nueva +=" "+ palabra 
    return (cadena_nueva)

c = "Quiero comer manzanas, solamente manzanas."
b = input("ingrese que palabra busca: ")
print(buscador(c,b))


