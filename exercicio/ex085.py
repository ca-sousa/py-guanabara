numeros = [[], []]

for p in range(1, 8):
    num = int(input('Digite um numero: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
        
numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
