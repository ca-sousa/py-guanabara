d = int(input('Por quantos dias voce alugou o carro?'))
km = float(input('Quantos KM voce rodou com o carro?'))

valor = (d * 60) + (km * 0.15)

print('O total a pagar e de R${:.2f}'.format(valor))