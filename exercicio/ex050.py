soma = 0 

for n in range(0, 6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0 :
        soma += num

if soma == 0:
    print('Nao foram escritos numeros pares')
else:
    print('A soma dos numeros pares e igual a {}'.format(soma))