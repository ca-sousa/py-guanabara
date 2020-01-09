import random

print('--=--='*15)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('--=--='*15)

rand = random.randint(0, 10)
num = int(input('Em que numero eu pensei?'))
cont = 1

if num == rand: 
    print('Parabens! Voce conseguiu me vencer! Pois pensei no numero {}'.format(rand))
else:
    while rand != num:
        print('Nao e esse numero! :(')
        cont += 1
        if num > rand:    
            num = int(input('Mais baixo... Digite outro numero: '))
        elif rand > num:
            num = int(input('Mais alto... Digite outro numero: '))

print('Parabens, voce acertou o numero que eu pensei foi {}, foram necessarias {} tentativas'.format(rand, cont))
