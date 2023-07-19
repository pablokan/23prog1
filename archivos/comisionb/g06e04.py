def inputStr(msg, mini=0, maxi=10**308):
    s = ''
    while not mini <= len(s) <= maxi:
        s = input(msg)




p0 = inputStr('Password (entre 5 y 8 caracteres): ', 5, 8)
p1 = inputStr('Password (al menos 4): ', 4)
p2 = inputStr('Password (a lo sumo 5): ', maxi=5)
p3 = inputStr('Password (sin rango): ')
