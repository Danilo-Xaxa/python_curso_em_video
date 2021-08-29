def ficha(nome=0, gols=0):
    nome = input('Nome do jogador: ')
    gols = input('Quantos gols ele fez? ')
    if not nome:
        nome = '<desconhecido>'
    if not gols:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


ficha()