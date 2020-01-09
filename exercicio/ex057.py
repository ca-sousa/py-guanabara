sexo = str(input('Informe o seu sexo: [M/F]')).upper().strip()

while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe o seu sexo: ')).upper().strip( )

print('Sexo {} registrado com sucesso'.format(sexo))