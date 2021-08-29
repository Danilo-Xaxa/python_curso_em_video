import random
import time
a = ['cara', 'coroa']
b = random.choice(a)
print('Seja bem-vindo ao jogo cara ou coroa! ')
print('Eu, o computador, irei jogar uma moeda virtual para o alto.')
print('Você tentará adivinhar se caiu cara ou coroa.')
y = input('Preparado? ')
if y == 'sim':
    time.sleep(1)
    print('*Jogando a moeda*')
    time.sleep(1)
    c = str(input('Pronto, joguei. Deu cara ou coroa? '))
    if b in c:
        print('Parabéns, você acertou!')
    else:
        print(f'Errou, caiu {b}. Tente de novo!')
else:
    print('Quando estiver preparado, é só avisar!')
#começando a usar o time