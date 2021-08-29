def aumentar(x, y, z):
    x = x + ((x / 100) * y)
    if z:
        x = f'R${int(x)},00'
    return x
def diminuir(x, y, z):
    x = x - ((x / 100) * y)
    if z:
        x = f'R${int(x)},00'
    return x
def dobrar(x, z):
    x = x * 2
    if z:
        x = f'R${int(x)},00'
    return x
def metade(x, z):
    x = x / 2
    if z:
        x = f'R${int(x)},00'
    return x
def monetario(x):
    x = f'R${int(x)},00'
    return x
def resumo(a, b, c):
    print('-' * 35)
    print(' ' * 13, 'RESUMO')
    print('-' * 35)
    print(f'Preço analisado: \t{monetario(a)}')
    print(f'Dobro do preço: \t{dobrar(a, True)}')
    print(f'Aumento de {b}%: \t{aumentar(a, b, True)}')
    print(f'Aumento de {c}%: \t{diminuir(a, c, True)}')
    print(f'Metade do preço: \t{metade(a, True)}')
    print('-' * 35)