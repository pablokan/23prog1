def mover_robot(pasos):
    # Coordenadas iniciales
    x = 0
    y = 0

    # Variable que indica hacia dónde mira el robot
    # 1 = hacia la parte positiva del eje y
    # -1 = hacia la parte negativa del eje y
    direccion = 1

    # Bucle para recorrer la lista de pasos
    for i in pasos:
        # Si i es positivo, el robot se mueve hacia adelante
        if i > 0:
            # Si el robot está mirando hacia la parte positiva del eje y,
            # se mueve hacia arriba en el eje y
            if direccion == 1:
                y += i
            # Si el robot está mirando hacia la parte negativa del eje y,
            # se mueve hacia abajo en el eje y
            else:
                y -= i
        # Si i es negativo, el robot se mueve hacia atrás
        else:
            # Si el robot está mirando hacia la parte positiva del eje y,
            # se mueve hacia abajo en el eje y
            if direccion == 1:
                y -= abs(i)
            # Si el robot está mirando hacia la parte negativa del eje y,
            # se mueve hacia arriba en el eje y
            else:
                y += abs(i)

        # Girar el robot 90 grados en sentido contrario a las agujas del reloj
        direccion *= -1

    # Coordenadas finales
    x = -y
    y = x - y

    # Devolver coordenadas finales
    return {'x': x, 'y': y}

# Lista de prueba
pasos = [10, 5, -2]

# Llamamos a la función para mover el robot y obtener las coordenadas finales
coordenadas_finales = mover_robot(pasos)

# Mostramos las coordenadas finales
print("Coordenadas finales:", coordenadas_finales)
