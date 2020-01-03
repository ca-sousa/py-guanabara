num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro valor e maior')
elif num2 > num1:
    print('O segundo valor e maior')
else:
    print('Nao existe valor maior, os dois sao iguais')