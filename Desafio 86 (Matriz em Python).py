listona = [[], [], [], [], [], [], [], [], []]
chave_listona1 = 0
for x in range(9):
    listona[x].append(int(input(f'Digite o {x + 1}º número: ')))
for x in range(9):
    print(listona[chave_listona1], end='')
    if x == 2 or x == 5 or x == 8:
        print('')
    chave_listona1 += 1
