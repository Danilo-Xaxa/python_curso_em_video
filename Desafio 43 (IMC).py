a = float(input('Diga seu peso: '))
b = float(input('Diga sua altura: '))
imc = a/(b**2)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso ideal.')
elif imc >= 30 and imc < 40:
    print('Você está na faixa da obesidade.')
elif imc >= 40:
    print('Você está na faixa da obesidade mórbida.')
#começando a usar o and