peso = float(input('Digite o seu peso(Kg): '))
altura = float(input('Digite a sua altura(m): '))

imc = peso / (altura*altura)

print(imc)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')