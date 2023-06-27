""" with open('montoto.txt', 'w') as monty:
    monty.write('josé manuel morete\notra cosa')

with open('montoto.txt', 'a') as monty:
    monty.write('\ntercera línea')

lista = ['\nfila1', '\nfila2']
with open('montoto.txt', 'a') as monty:
    monty.writelines(lista)
 """

with open('montoto.txt', 'w') as monty:
    monty.write('josé manuel morete\notra cosa\n')
    monty.write('josé manuel morete\notra cosa\n')    
