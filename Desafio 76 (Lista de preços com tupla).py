x = ('Pirulito', f'R${1},00', 'Cerveja', f'R${5},00',
     'Pizza', f'R${10},00', 'Hambúrguer', f'R${15},00',
     'Xampu', f'R${20},00', 'Queijo', f'R${25},00',
     'Peixe', f'R${30},00', 'Nesfits', f'R${40},00')
print('-'*40)
print(' '*11, 'LISTA DE PREÇOS')
print('-'*40)
a = 0
while a != len(x):
    print(x[a], '.'*(38-len(x[a])-len(x[a+1])), x[a+1])
    a += 2
print('-'*40)