n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))

tupla = (n1, n2, n3, n4)

print(f'\nOs valores digitados foram {tupla}')
print(f'O numero 9 foi digitado {tupla.count(9)} vezes')
print(f'O numero 3 apareceu na {tupla.index(3)+1} posicao')
print('Os numeros pares foram ', end='')
for c in range(0, len(tupla)):
    if tupla[c] % 2 ==0:
        print(tupla[c], end=' ')        
