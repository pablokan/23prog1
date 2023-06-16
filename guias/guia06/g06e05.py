from g06e04 import inputStr

def inputUser(msg):
    validado = False
    while not validado:
        u = inputStr(msg, mini=8)
        v1 = set('#$%&').intersection(set(u))
        v2 = set('1234567890').intersection(set(u))
        v3 = set('abcdefghijklmnopqrstuvwxyz').intersection(set(u))
        if len(v1)>0 and len(v2)>0 and len(v3)>0:
            validado = True

usuario = inputUser('Ingrese un nombre de usuario válido (debe contener como mínimo una letra, un dígito y al menos uno de estos caracteres especiales:  #, $, %, &): ')


