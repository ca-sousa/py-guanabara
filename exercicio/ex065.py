r = 'S'
cont = soma = maior = menor =0

while r == 'S':
    num = int(input('Digite um numero: '))
    r = input('Quer continuar? [S/N]').upper()
    if cont == 0:   
        cont = 1
        soma = num
        maior = num
        menor = num
    else:
        cont += 1
        soma += num 
        if maior < num:
            maior = num
        elif menor > num:
            menor = num

print('Voce digitou {} numeros e a media foi {}'.format(cont, (soma / cont)))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))