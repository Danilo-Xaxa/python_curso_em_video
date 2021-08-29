notas50 = notas20 = notas10 = notas1 = 0
print('=' * 20)
print('     BANCO CEV')
print('=' * 20)
valor = int(input('Que valor você quer sacar? R$'))

while valor >= 50:
    notas50 += 1
    valor -= 50

while valor >= 20:
    notas20 += 1
    valor -= 20

while valor >= 10:
    notas10 += 1
    valor -= 10

while valor >= 1:
    notas1 += 1
    valor -= 1

print(notas50, notas20, notas10, notas1)
