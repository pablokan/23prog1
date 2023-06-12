
lista = [1,2,3]
lista[1] = "dos" # es mutable (modificable)
print(lista)

tupla = (1,2,3)
#tupla[1] = "dos" da error porque las tuplas son Inmutables
print(tupla)
for x in range(len(tupla)): # pero se pueden recorrer igual que una lista
    print(tupla[x])
    
