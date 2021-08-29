a = float(input('Qual é o seu atual salário? '))
if a > 1250:
    print(f'Seu novo salário é {a+(a/10)}')
if a <= 1250:
    print(f'Seu novo salário é {a+(a/100*15)}')
#começando a usar o <=