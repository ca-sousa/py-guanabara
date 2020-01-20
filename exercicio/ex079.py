lista = list()

while True:
    num = int(input('Digite um numero: '))
    
    if num in lista:
        print('Numero ja existe')
    else:
        lista.append(num)
    
    opt = input('Deseja continuar? [S/N]')
    if opt.upper() == 'N':
        break

lista.sort()
print(f'Sua lista foi {lista}')
