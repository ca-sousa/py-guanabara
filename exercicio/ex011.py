largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))

area = largura * altura
tinta = area / 2

print('Sua parede tem as dimensao de {}x{} que gera uma area de {}m²'.format(largura, altura, area))
print('Para pintar esta parede, voce precisara de {}l de tinta'.format(tinta))