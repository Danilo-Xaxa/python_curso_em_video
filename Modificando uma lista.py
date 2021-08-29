lista = [3, 8, 2, 7, 1, 5, 4]
x = 0
print(f'Essa daqui é a lista original: {lista}.')
lista[5] = 9
x += 1
print(f'Essa daqui é a lista modificada {x} vez: {lista}.')
lista.append(5)
x += 1
print(f'Essa daqui é a lista modificada {x} vezes: {lista}.')
lista.insert(4, 6)
x += 1
print(f'Essa daqui é a lista modificada {x} vezes: {lista}.')
lista.sort(reverse=True)
x += 1
print(f'Essa daqui é a lista modificada {x} vezes: {lista}.')
lista.sort()
x += 1
print(f'Essa daqui é a lista modificada {x} vezes: {lista}.')