jogador = {}
gols = []
jogador['Nome'] = input('Nome do jogador: ')
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for x in range(jogador['Partidas']):
    a = int(input(f'Quantos gols foram feitos na {x+1}ª partida? '))
    gols.append(a)
    jogador['Gols'] = gols[:]
print('-' * 50)
for key, value in jogador.items():
    print(f'{key}: {value}')
print('-' * 50)
print(f'{jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for x in range(jogador['Partidas']):
    print(f'-> Na {x+1}º partida, ele fez {gols[x]} gols')
print(f'Total: {sum(gols)} gols')
