salario = float(input('Qual e o salario do Funcionario? R$  '))

if salario > 1250.00:
    novo =  salario + (salario * 0.10)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(salario, novo))
else:
    novo = salario + (salario * 0.15)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(salario, novo))

