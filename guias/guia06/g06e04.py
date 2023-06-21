def inputStr(msg, mini=float('-inf'), maxi=float('inf')):
    validado = False
    while not validado:
        s = input(msg)
        if mini <= len(s) <= maxi:
            validado = True
    return s


if __name__ == '__main__':
    nombreUsuario = inputStr('Nombre de usuario (entre 5 y 8 caracteres): ', 5, 8)
    print(nombreUsuario, 'aceptado')
    password1 = inputStr('Password (al menos 4): ', 4)
    password2 = inputStr('Password (a lo sumo 5): ', maxi=5)
    password3 = inputStr('Password (sin rango): ')
