preco = float(input('Valor total: R$'))

print('Formas de Pagamento \n'
    '[ 1 ] A vista dinheiro/cheque \n'
    '[ 2 ] A vista no cartao \n'
    '[ 3 ] Ate 2x no cartao \n'
    '[ 4 ] 3x ou mais no Cartao')

opt = int(input('Digite a forma de pagamento: '))

if opt == 1:
    final = preco - (preco * 0.10)
    print('Compra de R${:.2f} custara R${:.2f} no final'.format(preco, final))
    print('Desconto de R${:.2f}'.format(preco - final))
elif opt == 2:
    final = preco - (preco * 0.05)
    print('Compra de R${:.2f} custara R${:.2f} no final'.format(preco, final))
    print('Desconto de R${:.2f}'.format(preco - final))
elif opt == 3:
    print('Nao possui desconto. Valor final R${:.2f}'.format(preco))
elif opt == 4:
    parcela = int(input('Quantas parcelas?'))
    final = preco + (preco * 0.20)
    print('Sua compra parcelada em {}x de R${:.2f} com JUROS de R${}'.format(parcela, (final / parcela), (final - preco)))
    print('Compra de R${:.2f} custara R${:.2f} no final'.format(preco, final))
else:
    print('Opcao escolhida invalida')