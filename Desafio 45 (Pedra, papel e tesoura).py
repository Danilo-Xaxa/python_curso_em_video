from time import sleep
from random import randint


print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

entrada = int(input('Qual é a sua jogada? '))

print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO')
sleep(0.3)

print('-=' * 10)
lista = ['pedra', 'papel', 'tesoura']
jogador = lista[entrada]
computador = lista[randint(0, 2)]

print(f'Computador tirou {computador}')
print(f'Jogador tirou {jogador}')
print('-=' * 10)

if computador == 'pedra' and jogador == 'papel':
    print('JOGADOR VENCE')
elif computador == 'pedra' and jogador == 'tesoura':
    print('COMPUTADOR VENCE')
elif computador == 'papel' and jogador == 'pedra':
    print('COMPUTADOR VENCE')
elif computador == 'papel' and jogador == 'tesoura':
    print('JOGADOR VENCE')
elif computador == 'tesoura' and jogador == 'pedra':
    print('JOGADOR VENCE')
elif computador == 'tesoura' and jogador == 'papel':
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')
