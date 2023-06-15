# Escribe una función que cuente la cantidad de ocurrencias de una subcadena en una cadena de texto, permitiendo especificar si se debe realizar una búsqueda sin distinguir mayúsculas y minúsculas. 

frase = 'Desde niña me encanta mirar la luna, por eso es que le puse de nombre Luna a mi hija'

def contarSubCadena(cadena, subcadena, ignorarMayusculas=True):
    if ignorarMayusculas:
        cadena = cadena.lower()
    return cadena.count(subcadena)
    
print(contarSubCadena(frase, 'luna'))
print(contarSubCadena(frase, 'luna', ignorarMayusculas=False))
