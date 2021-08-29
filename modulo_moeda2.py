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

#x é o valor/preço/quantia, y é a taxa e z é a opção de transformar em dado monetário ou não