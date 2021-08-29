def aumentar(x, y):
    x = x+((x / 100) * y)
    return x
def diminuir(x, y):
    x = x - ((x / 100) * y)
    return x
def dobrar(x):
    x = x * 2
    return x
def metade(x):
    x = x / 2
    return x
def moeda(x):
    x = f'R${x}'
    return x