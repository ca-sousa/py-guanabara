from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(''' Suas opcoes: 
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

print('-'*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-'*20)

if computador == 0: #COMP PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada Invalida')
elif computador == 1: #COMP PAPEL
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Invalida')
elif computador == 2: #COMP TESOURA
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida')