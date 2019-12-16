preco = float(input('Qual o preco do produto? R$'))

novoP = preco - (preco*5/100)

print('O produto que custava R${:.2f}, na promocao com desconto de 5% custara R${:.2f}'.format(preco, novoP))