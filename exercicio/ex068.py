from random import randint

comp = soma = cont = 0

print('Par ou Impar')

while True:
    num = int(input('Diga um valor: [0-10]'))
    choice = input('Par ou Impar? [P/I] ').upper()
    comp = randint(0, 10)
    soma = num + comp

    print(f'Voce jogou {num} a maquina {comp}, resultando em {soma}')

    if choice == 'P' and soma % 2 == 0:
        print('Jogador ganhou!')
        print('Vamos jogar novamente!')
        cont += 1
    else:
        print('Maquina ganhou!')
        break

print(f'Voce teve {cont} vitorias consecutivas!')
