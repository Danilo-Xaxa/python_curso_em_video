a = float(input('Diga sua primeira nota: '))
b = float(input('Diga sua segunda nota: '))
c = (a+b)/2
print(f'Sua média é {c}')
if c >= 7:
    print('Parabéns, você passou.')
if c < 7:
    print('Infelizmente você não passou. Estude mais!')