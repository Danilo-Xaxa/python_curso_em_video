a = float(input('Diga sua primeira nota: '))
b = float(input('Diga sua segunda nota: '))
c = (a+b)/2
if c < 5:
    print(f'Sua média é {c} e você está reprovado.')
elif c >= 7:
    print(f'Sua média é {c} e você está aprovado.')
else:
    print(f'Sua média é {c} e você está em recuperação.')
