num1= float(input('Digite um valor: '))
num2= float(input('Digite um valor: '))

print(''' Menu: 
        [ 1 ] Somar 
        [ 2 ] Multiplicar 
        [ 3 ] Mostrar o maior 
        [ 4 ] Novos números 
        [ 5 ] Sair do programa''')
opt = int(input('Escolha uma opcao: '))

while opt != 5:
    if opt == 1:
        print('A soma dos numeros e de {}'.format(num1 + num2))
    elif opt == 2:
        print('A multiplicacao dos numeros e de {}'.format(num1 * num2))
    elif opt == 3:
        if num1 > num2:
            print('O numeor maior e {}'.format(num1))
        else: 
            print('O numeor maior e {}'.format(num2))
    elif opt == 4:
        num1= float(input('Digite um valor: '))
        num2= float(input('Digite um valor: '))
    else:
        print('Opcao invalida...')
        
    opt = int(input('Escolha uma opcao: '))

print('Obrigada por usar o nosso programa!')
