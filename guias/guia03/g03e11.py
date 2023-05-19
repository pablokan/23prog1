nombres = ["Ana", "Luis", "Juan"]
fecNac = ["13-05-1987", "01-12-2010", "23-01-2001"]

diaHoy = 20
mesHoy = 5
aniHoy = 2023
for x in range(len(nombres)):
    diaNac = int(fecNac[x][:2])
    mesNac = int(fecNac[x][3:5])
    aniNac = int(fecNac[x][-4:])
    edad = aniHoy - aniNac
    if mesNac > mesHoy or mesNac == mesHoy and diaNac > diaHoy:
        edad -= 1
    if edad >= 18:
        print(nombres[x])


