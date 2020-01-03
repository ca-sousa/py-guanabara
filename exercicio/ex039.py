from datetime import date

ano = int(input('Digite o ano de nascimento: '))

idade = date.today().year - ano

if idade == 18:
    print('Esta na hora de se alistar')
elif idade < 18:
    print('Ainda faltam {} anos para o seu alistamento'.format(18 - idade))
elif idade > 18:
    print('O prazo para alistamento passou ja faz {} anos'.format(idade - 18))