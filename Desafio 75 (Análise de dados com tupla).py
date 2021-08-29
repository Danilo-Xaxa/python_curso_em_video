x = (int(input('Insira um valor entre 0 e 10: ')),
    int(input('Insira outro valor entre 0 e 10: ')),
    int(input('Insira mais um valor entre 0 e 10: ')),
    int(input('Insira o último valor entre 0 e 10: ')))
if x.count(9) == 1:
    print(f'O número 9 apareceu 1 vez.')
elif x.count(9) == 0:
    print(f'O número 9 não apareceu nenhuma vez.')
else:
    print(f'O número 9 apareceu {x.count(9)} vezes.')
if 3 in x:
    print(f'O número 3 foi digitado na {(x.index(3))+1}ª vez.')
else:
    print(f'O número 3 não foi digitado.')
y = 0
while y != 4:
    if x[y] % 2 == 0:
        print(f'{x[y]} é par.')
    y += 1
#FALTA: ISSO DE SER PAR OU NÃO