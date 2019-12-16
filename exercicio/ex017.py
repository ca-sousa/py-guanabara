import math 

co = float(input('Qual o tamanho do cateto oposto: '))
ca = float(input('Qual o tamanho do cateto adjacente: '))

print('O hipotenusa vai medir {:.2f}'.format(math.hypot(ca, co)))