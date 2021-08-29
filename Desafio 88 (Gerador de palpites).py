from random import randint


matriz = []

jogos = int(input('Quantos jogo você quer que eu sorteie? '))

for counter in range(jogos):
    lista = []
    for a in range(6):
        lista.append(randint(1, 60))
    matriz.append(lista)

for lista in matriz:
    lista.sort()
    print(lista)
