from math import sqrt


a = float(input('Qual é o comprimento do primeiro cateto? '))
b = float(input('Qual é o comprimento do segundo cateto? '))

c = sqrt(a**2 + b**2)

print(f'O comprimento da hipotenusa é de {c:.1f}')
