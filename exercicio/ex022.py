nome = input('Digite seu nome completo: ')

splitado = nome.split()

print('Seu nome em maiusculo e {}'.format(nome.upper()))
print('Seu nome em minusculo e {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome e {}'.format(splitado[0]))