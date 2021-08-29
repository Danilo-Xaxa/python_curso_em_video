x = input('Você está precisando de reposição hormonal? ')
if x == 'sim':
    a = input('Sexo: ')
    if a == 'masculino':
        print('\033[0;34mTome testosterona\033[m')
    if a == 'feminino':
        print('\033[0;31mTome estrogênio\033[m')
    if a == 'todo dia':
        print('Engraçadinho viadinho')
if x == 'não':
    print('Bom saber! Se precisar, é só falar.')