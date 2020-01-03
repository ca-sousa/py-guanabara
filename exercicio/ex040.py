np1 = float(input('Digite a nota da NP1:'))
np2 = float(input('Digite a nota da NP2:'))

media = (np1 + np2)/2

print('Media: {}'.format(media))

if media < 5.0:
    print('Reprovado')
elif media >= 7.0:
    print('Aprovado')
elif 7 > media >= 5:
    print('Recuperacao')