from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6),}
print('-' * 40)
print(' ' * 10, 'JOGO DOS DADOS:')
for k, v in jogo.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print('-' * 40)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(' ' * 7, 'RANKING DOS JOGADORES:')
for i, v in enumerate(ranking):
    print(f'{i+1}º colocado: {v[0]}, que tirou {v[1]}.')
    sleep(1)
print('-' * 40)