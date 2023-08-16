nacidos2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

nacidos2008 = nacidos2008.split(',')

mujeres2008 = []
varones2008 = []

for i in range(len(nacidos2008)):
    if nacidos2008[i] == 'f':
        mujeres2008.append([int(nacidos2008[i-1]), nacidos2008[i-2]])
    elif nacidos2008[i] == 'm':
        varones2008.append([int(nacidos2008[i-1]), nacidos2008[i-2]])

mujeres2008.sort(reverse=True)
varones2008.sort(reverse=True)

mujeres2008.insert(0, [0, 'z'])
varones2008.insert(0, [0, 'zz'])

# [[18813, 'Emma'], [18616, 'Julia'], [17434, 'Emily'], [17081, 'Olivia'], [17039, 'Eva']]
# [[22594, 'Jacob'], [20626, 'Michael'], [20216, 'Ethan'], [19205, 'Joshua'], [19005, 'Daniel']]

mujeres2018 = [[0, 'zzz'], [18688, 'Emma'], [17921, 'Olivia'], [14924, 'Ava'], [14464, 'Isabella'], [13928, 'Sophia']] 
varones2018 = [[0, 'zzzz'], [19837, 'Liam'], [18267, 'Noah'], [14516, 'Michael'], [13525, 'James'], [13389, 'Oliver']]

sexo = 'f'
posicion = 2

if sexo == 'f':
    print(f'Mujeres en posicion {posicion}')
    dife = mujeres2008[posicion][0] - mujeres2018[posicion][0]
    if dife > 0:
        print(f'{mujeres2008[posicion][1]} de 2008 tiene {dife} mas que {mujeres2018[posicion][1]} de 2018')
    else:
        print(f'{mujeres2018[posicion][1]} tiene {-dife} mas que {mujeres2008[posicion][1]}')
elif sexo == 'm':
    print(f'Varones en posicion {posicion+1}')
    dife = varones2008[posicion][0] - varones2018[posicion][0]
    if dife > 0:
        print(f'{varones2008[posicion][1]} de 2008 tiene {dife} mas que {varones2018[posicion][1]} de 2018')
    else:
        print(f'{varones2018[posicion][1]} tiene {-dife} mas que {varones2008[posicion][1]}')

inicial = 'J'
todos = mujeres2008 + mujeres2018 + varones2008 + varones2018

for b in todos:
    if b[1][0] == inicial:
        print(b[1])

print('3) Nombres que se repiten')
for e in varones2008:
    for f in varones2018:
        if e[1] == f[1]:
            print(e[1])

for e in mujeres2008:
    for f in mujeres2018:
        if e[1] == f[1]:
            print(e[1])