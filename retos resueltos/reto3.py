c = 0
for ap in range(2):
    if ap == 0:
        ampm = "am"
    else:
        ampm = "pm"

    for h in range(12):
        if h == 0:
            horas = "12"
        else:
            horas = str(h)
        for m in range(4):
            c = c + 1
            print(c, ')', end='')
            mi = m * 15
            if mi == 0:
                minutos = "00"
            else:
                minutos = str(mi)
            print(horas + ':' + minutos + " " + ampm)
