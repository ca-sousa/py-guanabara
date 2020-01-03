valor =  float(input('Digite o valor da Casa que deseja comprar: R$'))
salario = float(input('Digite o seu salario: R$'))
tempo = int(input('Em quantos anos deseja pagar a casa? '))

prest = valor / (tempo * 12)

print('Analisando as informacoes: \n'
    'Temos {} anos para efetuar o pagamento de uma casa no valor de R${:.2f} com a renda de R${:.2f}, gera uma prestacao de R${:.2f}'
    .format(tempo, valor, salario, prest))
if prest > (salario * 0.30):
    print('O emprestimo foi NEGADO')
else:
    print('O emprestimo foi APROVADO')