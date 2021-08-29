from random import randint


sim_ou_nao = input('''Olá, sou seu computador!
Acabei de pensar em um número entre 1 e 10, quer tentar adivinhar qual é? ''').lower().strip()

if sim_ou_nao == 'sim' or sim_ou_nao == 's':
    computador = randint(1, 10)
    acertou = False
    palpites = 0

    while not acertou:
        jogador = int(input('Seu palpite: '))
        palpites += 1

        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('É mais, tente de novo.')
            elif jogador > computador:
                print('É menos, tente de novo.')

    print(f'Parábens! Você acertou com {palpites} tentativas.')

else:
    print('Quando quiser jogar, estarei aqui!')
