matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = scol = mai = 0

for f in range(0, 3):
    for d in range(0, 3):
        matriz[f][d] = int(input('Digite um valor: '))

print('-'*50)

for f in range(0, 3):
    for d in range(0, 3):
        print(f'[ {matriz[f][d]} ]', end='')
        if matriz[f][d] % 2 == 0:
            soma += matriz[f][d]
    print()

print('-'*50)
print(f'Soma de todos os numeros pares {soma}')

for f in range(0, 3):
    scol += matriz[f][2]
print(f'A soma dos valores da terceira coluna e {scol}')

for d in range(0, 3):
    if d == 0:
        mai = matriz[1][d]
    elif matriz[1][d] > mai:
        mai = matriz[1][d]
print(f'O maior valor da segunda linha e {mai}')