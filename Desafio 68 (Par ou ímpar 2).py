from random import randint


print('_'*150)
print('''*** Seja bem-vindo ao jogo de par ou ímpar ***
Eu, o seu computador, vou jogar um número e você também.''')

vitorias_usuario = 0

while True:
    computador = randint(1, 10)
    print('-' * 60)
    par_ou_impar = input('Par ou ímpar? ').strip().upper()

    if par_ou_impar == 'PAR':
        usuario = int(input('Ok, jogue um número: '))
        soma_dedos = computador + usuario

        if soma_dedos % 2 == 0:
            print(f'Deu par, você venceu! Eu tinha escolhido o número {computador}.')
            vitorias_usuario += 1
        else:
            print(f'Deu ímpar, eu venci! Eu tinha escolhido o número {computador}.')
            break

    elif par_ou_impar == 'ÍMPAR' or par_ou_impar == 'IMPAR':
        usuario = int(input('Ok, jogue um número: '))
        soma_dedos = computador + usuario

        if soma_dedos % 2 == 0:
            print(f'Deu par, eu venci! Eu tinha escolhido o número {computador}.')
            break
        else:
            print(f'Deu ímpar, você venceu! Eu tinha escolhido o número {computador}.')
            vitorias_usuario += 1

if vitorias_usuario > 1:
    print(f'Você ganhou de mim {vitorias_usuario} vezes consecutivas!')
