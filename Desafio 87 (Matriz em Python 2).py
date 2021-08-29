print('-'*40)
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for x in range(3):
    matriz[x][0] = int(input(f'Digite um valor para [{x}, 0]: '))
    matriz[x][1] = int(input(f'Digite um valor para [{x}, 1]: '))
    matriz[x][2] = int(input(f'Digite um valor para [{x}, 2]: '))

print('-'*40)
for y in matriz:
    print(y)

print('-'*40)
pares = 0

for par in matriz:
    for z in par:
        if z % 2 == 0:
            pares += z

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {(matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
