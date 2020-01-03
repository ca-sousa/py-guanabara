nome = input('Qual o seu nome? ')

if nome == 'Carla':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome e comum no Brasil')

print('Tenha um bom dia, {}!'.format(nome))