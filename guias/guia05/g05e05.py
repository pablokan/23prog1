frase = "Quiero comer manzanas, solamente manzanas."

def listaPalabras(s):
    sinPuntuacion = ""
    for caracter in s:
        if caracter not in ".,":
            sinPuntuacion += caracter
    return sinPuntuacion.split()

def masLarga(lista):
    masLarga = ""
    for palabra in lista:
        if len(palabra) > len(masLarga):
            masLarga = palabra
    return masLarga, len(masLarga)

print(listaPalabras(frase))
palabraMasLarga, longitud = masLarga(listaPalabras(frase))
print("La palabra más larga es: ", palabraMasLarga, "y su longitud es: ", longitud )

