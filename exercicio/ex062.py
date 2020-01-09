print('Fazendo PA')

num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razao: '))
termo = num
cont = 1
total = 0
mais = 10 

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += raz
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))
print('Progressao finalizada com {} termos mostrados'.format(total))