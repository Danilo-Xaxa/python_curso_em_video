a = []
x = 'sim'
while x == 'sim' or x == 's':
    a.append(int(input('Digite um número: ')))
    sim = input('Quer continuar? [S/N] ').strip().lower()
y = int(input('Qual número você quer saber se está dentro da lista? '))
if y in a:
    print(f'O número {y} está dentro sim!')
else:
    print(f'O número {y} não está na lista.')
print(f'No total, {len(a)} números foram digitados.')
a.sort(reverse=True)
print(f'Os números em ordem decrescente são: {a}.')
