numeros = [420, 69, 24, 666]
numeros.sort()
x = y = 0
while y != len(numeros):
    print(numeros[y], end='')
    if y != (len(numeros)-1):
        print(' → ', end='')
    x += 1
    y += 1

print('-'*32)

valores = [4, 2, 7, 3, 8, 1, 9, 5, 0, 6]
for lugar, valor in enumerate(valores):
    print(f'Na posição {lugar} encontrei o valor {valor}')

print('-'*32)

lista = []
for x in range(0, 5):
    lista.append(int(input('Digite um número: ')))
lista.sort()
print(lista)
