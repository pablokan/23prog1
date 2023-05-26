""" Tomar una fecha en formato "DD-MM-AAAA" y convertirla en "D de [Mes] de AAAA".
Ejemplo:
Entrada: 03-06-1965
Salida: 3 de junio del 1965 (si el día tiene una sola cifra hay que sacar el cero)
"""
fechaEntrada = '03-06-1965'
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dia = int(fechaEntrada[:2])
dia = str(dia)
iMes = int(fechaEntrada[3:5]) - 1 
mes = meses[iMes]
anio = fechaEntrada[6:]
fechaSalida = dia + ' de ' + mes + ' del ' + anio
print(fechaSalida)
