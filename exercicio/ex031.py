dist = float(input('Qual e a distancia da sua viagem? '))

print('Voce esta prestes a comecar uma viagem de {}Km'.format(dist))

if dist <= 200:
    passagem = dist * 0.50
    print('E o preco da sua passagem sera de R${:.2f}'.format(passagem))
else: 
    passagem = dist * 0.45
    print('E o preco da sua passagem sera de R${:.2f}'.format(passagem))


## Ou com condicao simples
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print('E o preco da sua passagem sera de R${:.2f}'.format(preco))
