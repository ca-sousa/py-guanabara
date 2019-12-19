import random

print('--=--='*15)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('--=--='*15)

num = int(input('Em que numero eu pensei?'))
rand = random.randint(0, 5)

print('PROCESSANDO...')

if num == rand: 
    print('Parabens! Voce conseguiu me vencer! Pois pensei no numero {}'.format(rand))
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}'.format(rand, num))
