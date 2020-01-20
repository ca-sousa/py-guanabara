lista = list()
cont = 0
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    
    cont += 1

    opt = input('Deseja continuar? [S/N]')
    if opt.upper() == 'N':
        break

lista.sort(reverse = True)
print(f'Foram digitados {cont} numeros')
#  podia ter usado len(lista)
print(f'Sua lista em ordem decrescente foi {lista}')

if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O Valor 5 nao foi encontrado')