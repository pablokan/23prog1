def calcularEdad(fechaNacimiento):
    fechaActual = (2023, 6, 30)

    anioActual, mesActual, diaActual = fechaActual
    anioNacimiento, mesNacimiento, diaNacimiento = fechaNacimiento

    edad = anioActual - anioNacimiento

    if (mesActual < mesNacimiento) or (mesActual == mesNacimiento and diaActual < diaNacimiento):
        edad -= 1

    return edad


with open("personas.txt", "r", encoding="utf-8") as archivoLectura:
    with open("mayores.txt", "w", encoding="utf-8") as archivoEscritura:
        archivoLectura.readline()
        for linea in archivoLectura:
            nombre, fechaNacimiento = linea.split(",")
            dia, mes, anio = [int(valor) for valor in fechaNacimiento.split("/")]
            #print(dia, mes, anio)
            fecha_nacimiento = (anio, mes, dia)
            edad = calcularEdad(fecha_nacimiento)
            print(edad)
            if edad >= 18:
                archivoEscritura.write(f"{nombre}, {edad}\n")
