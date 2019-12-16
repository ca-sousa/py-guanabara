salario = float(input('Qual e o salario do Funcionario?'))

novo = salario + (salario * 0.15)

print('O salario que era R${}, com aumento de 15% passara a receber R${:.2f}'.format(salario, novo))