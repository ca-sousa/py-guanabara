num = int(input('Digite um numero inteiro: '))

print('Escolha uma das bases para conversao:\n'
    '[ 1 ] Converter para Binario \n'
    '[ 2 ] Converter para Octal \n'
    '[ 3 ] Converter para Hexadecimal')

opt = int(input('Sua opcao: '))

if opt == 1:
   print('{} convertido para Binario e igual a {}'.format(num, bin(num) [2:]))
elif opt == 2:
   print('{} convertido para Binario e igual a {}'.format(num, oct(num) [2:]))
elif opt == 3:
   print('{} convertido para Binario e igual a {}'.format(num, hex(num) [2:]))
else:
    print('A opcao escolhida e inexistente')