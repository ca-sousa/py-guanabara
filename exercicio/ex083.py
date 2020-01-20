exp = input('Digite a expressao: ')
lista = []

for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')