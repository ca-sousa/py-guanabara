s = 0 
for n in range(1, 501):
    if n % 2 != 0:
        if n % 3 == 0:
            s += n

print('A soma de todos os numeros impares e divisiveis por 3 e {}'.format(s))

# OU

soma = 0 
print('Outro metodo')
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c

print('A soma de todos os numeros impares e divisiveis por 3 e {}'.format(soma))
