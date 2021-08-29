a = []
b = []
c = []
x = 'sim'
while x == 'sim' or x == 's':
    y = int(input('Digite um número: '))
    a.append(y)
    if y % 2 == 0:
        b.append(y)
    else:
        c.append(y)
    x = input('Quer continuar? [S/N] ').strip().lower()
print('')
print(f'Esta é a lista dos números pares: {b}')
print(f'Esta é a lista dos números ímpares: {c}')
print(f'Esta é a lista geral: {a}')

#ou

a = []
b = []
c = []
x = 'sim'
z = 0
while x == 'sim' or x == 's':
    y = int(input('Digite um número: '))
    a.append(y)
    x = input('Quer continuar? [S/N] ').strip().lower()
print('')
print(f'Esta é a lista geral: {a}')
while z != len(a):
    if a[z] % 2 == 0:
        b.append(a[z])
    else:
        c.append(a[z])
    z += 1
print(f'Esta é a lista dos números pares: {b}')
print(f'Esta é a lista dos números ímpares: {c}')
