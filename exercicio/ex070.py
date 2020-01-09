total = umk = barato = cont =  0
nome_b = resp = ''

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preco do produto: '))

    total += preco

    if preco > 1000:
        umk += 1

    if cont  == 0:
        barato = preco
        nome_b = nome
    else: 
        if barato > preco:
            barato = preco
            nome_b = nome
    cont += 1

    resp = input('Deseja continuar? [S/N]').upper()
    if resp == 'N':
        break

print(f'Total da compra R${total}')
print(f'Quantidade de produtos com o valor acima de R$1000: {umk}')
print(f'Produto mais barato: {nome_b}')