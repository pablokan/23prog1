def carga():
    from calculo_edad import edad
    lista = []
    with open('archivos/personas.txt') as archPersonas:
        archPersonas.readline()
        print(archPersonas.tell())
        lineas = archPersonas.readlines()
        print(lineas)
        for linea in lineas:
            fecha = linea.split()[1]
            e = edad(fecha) 
            if  e >= 18:
                l = linea.split()[0] + " " + str(e) + '\n'
                lista.append(l)
    return lista

def salida(lista):
    with open('mayores.txt', 'w') as archMayores:
        archMayores.write('Nombre, Edad\n')
        archMayores.writelines(lista)

salida(carga())

