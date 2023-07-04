# abrir el archivo1 para lectura y el archivo2 para escritura
with open('archivo1.txt', 'r') as archivo_lectura, open('archivo2.txt', 'w') as archivo_escritura:
    # Ahora puedes leer desde archivo_lectura y escribir en archivo_escritura
    # No necesitas cerrar los archivos explícitamente, 
    # la declaración with se encarga de eso automáticamente
