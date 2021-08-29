lista = []

quantos = int(input('Quantos números você quer adicionar na lista? '))

for c in range(quantos):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('O número digitado é a nova última posição da lista\n')
    else:
        for b in range(5):
            if num <= lista[b]:
                lista.insert(b, num)
                print(f'O número é a nova posição {b} da lista\n')
                break

print(f'A lista completa e em ordem é: {lista}')