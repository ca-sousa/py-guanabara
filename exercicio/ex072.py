tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um numero entre 0 e 20: '))

while num not in range(0, 21):
    if num > 20 or num < 0:
        num = int(input('Tente novamente.Digite um numero entre 0 e 20: '))

print(f'Voce digitou o numero {tupla[num]}')