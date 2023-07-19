with open('subcarpeta/subchoto.txt', 'w') as subchoto:
    subchoto.write('cualquiera')

with open('subcarpeta/subchoto.txt') as subchoto:
    print(subchoto.read(4))

