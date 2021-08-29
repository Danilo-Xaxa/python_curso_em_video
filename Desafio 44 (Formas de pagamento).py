valor = float(input('Qual é o preço normal do produto? '))

print('''
Formas de pagamento disponíveis:
[A] À vista no dinheiro ou cheque (10% de desconto)
[B] À vista no cartão (5% de desconto)
[C] Em até 2x no cartão (preço normal)
[D] A partir de 3x vezes no cartão (20% de juros)
''')

forma_pagamento = input('Qual é a forma de pagamento? ').strip().upper()

opc1 = valor - (valor / 10)
opc2 = valor - (valor / 20)
opc3 = valor
opc4 = valor + (valor / 5)

if forma_pagamento == 'A':
    print(f'O preço será de {opc1} reais.')
elif forma_pagamento == 'B':
    print(f'O preço será de {opc2} reais.')
elif forma_pagamento == 'C':
    print(f'O preço será de {opc3} reais.')
elif forma_pagamento == 'D':
    print(f'O preço será de {opc4} reais.')
else:
    print('erro')
