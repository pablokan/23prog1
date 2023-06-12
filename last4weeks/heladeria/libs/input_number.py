# Convertir inputInt a inputNumber. Dicha función debe permitir tomar un entero o un real.
# Piensen que cambios se requieren. En el algoritmo y en los parámetros

def inputNumber(tipo, cartel):
    validado = False
    while not validado:
        n = input(cartel)
        try:
            if tipo == "entero":
                n = int(n)
            elif tipo == "real":
                n = float(n)
            validado = True
        except:
            print("No es un", tipo)
    return n


if __name__ == "__main__":
    altura = inputNumber("real", "Ingrese su altura: ")
    edad = inputNumber("entero", "Ingrese su edad: ")
    