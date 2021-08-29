lista = []
continuar = 's'

print('-=' * 18)
while continuar == 'sim' or continuar == 's':
    nome = input('Nome: ')
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2)/2
    listona = [nome, [nota1, nota2], media]
    lista.append(listona)
    continuar = input('Quer continuar? [S/N] ').strip().lower()
    print('-='*18)

print('NUM     NOME          MÉDIA')
print('-' * 36)

for y, z in enumerate(lista):
    print(f'{y+1:<8}{z[0]:<14}{lista[y][2]:<8.1f}')
print('-' * 60)

while True:
    continuar = int(input('Quer saber as notas de qual aluno? (Digite 0 para encerrar) '))
    if continuar != 0:
        print(f'As notas de {lista[continuar - 1][0]} foram {lista[continuar - 1][1][0]} e {lista[continuar - 1][1][1]}')
        print('-'*60)
    else:
        print('-'*60)
        break