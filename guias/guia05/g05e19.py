def recuadrar(cadena):
    rv =  '║' 
    esd = '╗'
    eid = '╝'
    rh = '═'
    esi = '╔'
    eii = '╚'
    print(esi + rh * (len(cadena)+2) + esd)
    print(rv + ' ' + cadena + ' ' + rv)
    print(eii + rh * (len(cadena)+2) + eid)

recuadrar('River Plate')
recuadrar('una cadena más larga que la anterior')