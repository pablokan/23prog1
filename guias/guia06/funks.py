def inputInt(msg, errorMsg):
    validado = False
    while not validado:
        try:
            n = int(input(msg))
            validado = True
        except:
            print(errorMsg)
    return n
