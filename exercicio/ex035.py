print('Analisador de Triangulos:')
print('----'*15)

r1 = float(input('Primeiro Segmento:'))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM formar um triangulo!')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo!')