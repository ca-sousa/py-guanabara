print('Fazendo PA')

num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razao: '))

for n in range(1, 11):
    print('{} -> '.format(num), end='')
    num += raz

print('Acabou')

# outra forma

dec = num + (10 - 1) * raz
for c in range(num, dec + raz, raz):
    print('{} '.format(c), end='-> ')
print('Acabou')