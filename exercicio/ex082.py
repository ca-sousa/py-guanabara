lista = list()
listap = list()
listai = list()

while True:
    num = int(input('Digite um numero: '))
    lista.append(num)

    if num % 2 == 0:
        listap.append(num)
    if num % 2 != 0:
        listai.append(num)

    opt = input('Deseja continuar? [S/N]')
    if opt.upper() == 'N':
        break

print(f'Sua lista foi {lista}')
print(f'Lista de pares {listap}')
print(f'Lista de impares {listai}')