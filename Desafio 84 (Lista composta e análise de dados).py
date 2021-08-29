print('-'*150)
galera = []
dados = []
a = contador = 0
q = int(input('''Quantas pessoas você quer cadastrar?
(Se não sabe ainda, digite 0) '''))
if q == 0:
    x = 'sim'
    while x == 'sim' or x == 's':
        print('-' * 25)
        dados.append(input('Nome: '))
        dados.append(int(input('Peso: ')))
        galera.append(dados[:])
        dados.clear()
        x = input('Quer continuar? [S/N] ').strip().lower()
        contador += 1
    print('-' * 25)
    for x in range(contador):
        print(f'{galera[a][0]} tem {galera[a][1]} quilos.')
        a += 1
    print('-' * 25)
    print(f'{contador} pessoas foram cadastradas.')
else:
    for x in range(q):
        print('-'*15)
        dados.append(input('Nome: '))
        dados.append(int(input('Peso: ')))
        galera.append(dados[:])
        dados.clear()
    print('-' * 25)
    for x in range(q):
        print(f'{galera[a][0]} tem {galera[a][1]} quilos.')
        a += 1
    print('-' * 25)
    print(f'{q} pessoas foram cadastradas.')
