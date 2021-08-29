a = int(input('Qual é a distância, em quilômetros, da viagem? '))
if a < 200:
    print(f'O preço a ser pago é de {a/2} reais')
else:
    print(f'O preço a ser pago é de {(a/100)*45} reais')