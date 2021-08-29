bandas = ('red_hot', 'led_zeppelin',
     'pink_floyd', 'the_strokes',
     'the_beatles', 'arctic_monkeys',
     'muse', 'queen')
x = 0
vogais = ('a', 'e', 'i', 'o', 'u', 'y')
while x != (len(bandas)*(len(vogais))):
    y = 0
    print('')
    if x != len(bandas):
        print(f'Na banda {bandas[x]}, temos as vogais: ')
        while y != (len(vogais)):
            if vogais[y] in bandas[x]:
                print('-', vogais[y])
            y += 1
        x += 1
    else:
        break



#         SOLUÇÃO COM FOR:

#bandas = ('red_hot', 'led_zeppelin',
     #'pink_floyd', 'the_strokes',
     #'the_beatles', 'arctic_monkeys',
     #'muse', 'queen')
#for x in bandas:
#    print(f'\nNa palavra {x.upper()} temos: ', end='')
#    for letra in x:
#        if letra.lower() in 'aeiouy':
#            print(f'{letra};', end=' ')
