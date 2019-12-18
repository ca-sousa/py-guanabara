nome = input('Digite o seu nome completo: ')

splitado = nome.split()

print('Muito prazer em te conhecer')
print('Seu primeiro nome e {}'.format(splitado[0]))
print('Seu ultimo nome e {}'.format(splitado[len(splitado)-1]))