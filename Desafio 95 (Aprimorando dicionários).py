lista_mae = []
jogador = {}
gols = []
x = 'sim'
contador = 0
while x == 'sim' or x == 's':
    print('-' * 50)
    jogador['Nome'] = input('Nome do jogador: ')
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols = []
    for y in range(jogador['Partidas']):
        a = int(input(f'Quantos gols foram feitos na {y+1}ª partida? '))
        gols.append(a)
        jogador['Gols'] = gols
    contador += 1
    lista_mae.append(jogador.copy())
    x = input('Quer continuar? [S/N] ').strip().lower()
print('-' * 50)
print('NUM   NOME     GOLS     TOTAL')
for y in range(contador):
    print(f'{y+1}     {lista_mae[y]["Nome"]}   {lista_mae[y]["Gols"]}   {sum(lista_mae[y]["Gols"])}')
print('-' * 50)
contador = 0
while True:
    x = int(input('Mostrar os dados de qual jogador? (Use o número dele ou digite 0 para encerrar) '))
    if x != 0:
        if x <= len(lista_mae):
            x -= 1
            print(f'Dados de {lista_mae[x]["Nome"]}:')
            for y in range(lista_mae[x]["Partidas"]):
                print(f'-> Na {y + 1}º partida, ele fez {lista_mae[x]["Gols"][y]} gols')
            print(f'Total: {sum(lista_mae[x]["Gols"])} gols')
            print('-' * 50)
        else:
            print('ERRO! Digite um número válido')
            print('-' * 50)
    else:
        break