dados = []
pessoas = []
mai = men = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    opt = input('Deseja continuar? [S/N] ').upper()
    if opt == 'N':
        break

print('-'*50)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men}. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print()