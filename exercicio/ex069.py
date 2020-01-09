cont_id = cont_h = cont_m = 0

while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: [M/F]').upper()

    if idade > 18:
        cont_id += 1
    if sexo == 'M':
        cont_h += 1
    if sexo == 'F' and idade < 20: 
        cont_m += 1
    
    resp = input('Deseja continuar? [S/N]').upper()

    if resp == 'N':
        break

print('Analisando: ')
print(f'{cont_id} pessoas cadastradas tem mais de 18 anos')
print(f'{cont_h} homem(ns) foram cadastrados')
print(f'{cont_m} mulher(es) com menos de 20 anos foram cadastradas')