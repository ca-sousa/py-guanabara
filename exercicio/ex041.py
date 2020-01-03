from datetime import date

ano = int(input('Digite o seu ano de Nascimento:'))
idade = date.today().year - ano

print(idade)

if idade <= 9:
    print('Categoria MIRIM')
elif  idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19 :
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
elif idade > 25:
    print('Categoria MASTER') 