def suma(*args):
    t = 0
    for e in args:
        t += e
    print(t)

suma()

def saludo(nombre, ciudad='Rio Cuarto'):
    print('Hola', nombre, ' veo que sos de', ciudad)

saludo('Juan', 'San Basilio')
saludo('Ana')

def foo(p1, p2, n1='valor de n1', n2='valor de n2'):
    print(p1, p2, n1, n2)

foo(1,2, 'nuevo valor de n2')

