from random import randint
quant = num = 0 
lista = []
listaf = []

quant = int(input('Quantos jogos devo sortear? '))

while True:
    for c in range(0,6):
        num = randint(1, 60)
        lista.append(num)

    listaf.append(lista[:])
    lista.clear()

    quant -= 1
    if quant == 0: 
        break

print('Os jogos sorteados foram: ')
print(listaf)