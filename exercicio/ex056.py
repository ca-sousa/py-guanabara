soma_id = 0
maior = 0
nomeM = ''
cont = 0

for n in range(1, 5):
    print('---> {} Pessoa'.format(n))
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ').upper()

    # Somar idades para media
    soma_id += idade

    if n == 1:
        if sexo == 'M' or sexo == 'MASCULINO':
            maior = idade
            nomeM = nome

        if sexo == 'F' or sexo == 'FEMININO':
            if idade < 20:
                cont += 1
    
    else:
        if sexo == 'M' or sexo == 'MASCULINO' and maior < idade:
            maior = idade
            nomeM = nome
        if sexo == 'F' or sexo == 'FEMININO' and idade < 20:
            cont += 1
        

print('\n Analise final: \n')
print('A media de idade do Grupo e de {}'.format(soma_id / 4))
print('O nome do homem mais velho e {}'.format(nomeM))
print('O numero de mulheres com menos de 20 anos e de {}'.format(cont))