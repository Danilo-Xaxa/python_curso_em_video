def maior(*num):
    print('-' * 55)
    if len(num) >= 1:
        print('Valores computados: ', end='')
        for x in range(len(num)):
            print(num[x], end=' - ')
        print('FIM')
        print(f'São {len(num)} valores e o maior deles é {max(num)}.')
    else:
        print('Nenhum valor foi computado dessa vez.')
maior(2, 5, 8, 1)
maior(1, 2, 3, 4, 5)
maior(9, 8, 7)
maior(32, 77543, 643, 245)
maior()
print('-' * 55)