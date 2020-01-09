num = int(input('Digite um numero inteiro: '))

soma = 0
cont = 0

while num != 999:
    soma += num
    cont += 1
    print('Para sair digite 999')
    num = int(input('Digite um numero inteiro: '))

print('Foram digitados {} numeros, que geraram a soma de {}'.format(cont, soma))