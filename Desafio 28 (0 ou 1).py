import random
a = [0, 1]
b = random.choice(a)
x = input('Quer jogar um jogo? ')
if x == 'sim':
    print(
        'O jogo é de azar. Você irá digitar 0 ou 1, se você digitar o número que estou pensando, você ganha.\nVocê tem 50% de chances vencer e 50% de chances de perder. ')
    c = int(input('Digite 0 ou 1: '))
    if b == c:
        print('Parabéns, você acertou!')
    else:
        print(f'Errou, tente de novo! O número escolhido foi {b}')
if x == 'não':
    print('Certo. Quando quiser, é só dizer!')
#começando a usar o if e o else