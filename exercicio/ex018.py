import math 

ang = float(input('Digite o angulo que voce deseja: '))

print('O angulo de {} tem o Seno de {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('O angulo de {} tem a Tangente de {:.2f} '.format(ang, math.tan(math.radians(ang))))
