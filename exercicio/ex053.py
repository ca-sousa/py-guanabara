frase = input('Digite uma frase: ').replace(' ', '').upper()
inverso = frase[::-1]

print('O inverso de {} e {}'.format(frase, inverso))

if frase == inverso:
    print('A frase digitada eh um palindromo')
else: 
    print('A frase digitada nao eh um palindromo')

# O metodo que o professor utilizou foi mais complexo e que 
# necessitava de muitas mais linhas de codigo, caso queira ver:
# https://www.youtube.com/watch?v=5VBWe6BXzRo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=21