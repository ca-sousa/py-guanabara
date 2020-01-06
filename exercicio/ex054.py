from datetime import date

menor = 0
maior = 0

for n in range(1,8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(n)))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1 

print('Analisando este grupo de pessoas temos {} que nao atingiram a maioridade \n'
    'E temos {} que atingiram maioridade'.format(menor, maior))
