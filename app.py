peso = float(input('qual seu peso? '))
altura = float(input('qual sua altura? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'ABAIXO DO PESO, seu imc é {imc:.1f}')

elif imc < 25:
    print(f'PESO IDEAL, seu imc é {imc:.1f}')

elif imc < 30:
    print(f'SOBREPESO, seu imc é {imc:.1f}')

elif imc < 40:
    print(f'OBESIDADE, seu imc é {imc:.1f}')

else:
    print(f'OBESIDADE MORBIDA, seu imc é {imc:.1f}')