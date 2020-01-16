palavras = ('AVIAO', 'COELHO', 'BRUNO', 'CARLA', 'CACHORRO')

for n in range(0, len(palavras)):
    print(f'Na palavra {palavras[n]} temos ', end='')
    for l in palavras[n]:
        if l in 'AEIOU':
            print(l, end='') 
    print('\n')
