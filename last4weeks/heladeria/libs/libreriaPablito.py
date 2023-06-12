def inputInt(cartel):
    validado = False
    while not validado:
        n = input(cartel)
        try:
            n = int(n)
            validado = True
        except:
            print("No es un entero")
    return n

def foo():
    return "foo de libreria pablito"

if __name__ == "__main__":
    edad = inputInt("Ingrese una edad: ")    
    sueldo = inputInt("Ingrese su sueldo: ")

