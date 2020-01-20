cont = 1 
lista = list()
while cont <= 5:
    num = int(input('Digite um numero: '))
    lista.append(num)
    cont += 1

maior = max(lista)
menor = min(lista)

print(f'Sua lista foi {lista}')
print(f'O maior valor foi {maior} e esta na posicao {lista.index(maior)+1}')
print(f'O menor valor foi {menor} e esta na posicao {lista.index(menor)+1}')
