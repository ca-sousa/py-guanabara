city = input('Em que cidade voce nasceu? ').strip()

splitado = city.upper().split()

if splitado[0] == 'SANTO':
    print('True')
else:
    print('False')

# Jeito do professor:
print(city[:5].upper() == 'SANTO')