a = []
c = 'sim'
while c == 'sim' or c == 's':
    b = int(input('Digite um número: '))
    if b not in a:
        a.append(b)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não é possível adicioná-lo.')
    c = input('Quer continuar? [S/N] ').strip().lower()
a.sort()
print(f'Lista completa e ordenada: {a}.')
