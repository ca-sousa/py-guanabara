print('Fazendo PA')

num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razao: '))
cont = 0

while cont != 10:
    print('{} -> '.format(num), end='')
    num += raz
    cont += 1

print('Acabou')
