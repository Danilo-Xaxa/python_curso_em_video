a = [[], []]
#cria umas listas
for x in range(1, 8):
    y = int(input(f'Digite o {x}º número: '))
    if y % 2 == 0:
        a[0].append(y)
    else:
        a[1].append(y)
a[0].sort()
a[1].sort()
print(f'Números pares digitados: {a[0]}')
print(f'Números ímpares digitados: {a[1]}')