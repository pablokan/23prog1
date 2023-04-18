from random import choice
winC, winU = 0
while winC < 3 and winU < 3:
    computerChoice = choice(['piedra', 'papel', 'tijera'])
    userChoice = input('Ingrese su elección (piedra/papel/tijera): ')
    if computerChoice == userChoice:
        print('Empate')
    elif computerChoice == 'piedra':
        

