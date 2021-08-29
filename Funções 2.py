print('-' * 150)

help(input)

print('-' * 150)

print(input.__doc__)

print('-' * 150)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')


contador(4, 16, 2)
help(contador)

print('-' * 150)

def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}.')


soma(5, 7, 1)
soma(9, 2)
soma(4)
soma()

print('-' * 150)

def somando(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somando(3, 7, 4)
r2 = somando(2, 8)
r3 = somando(5)
print(f'Os resultados foram {r1}, {r2} e {r3}.')

print('-' * 150)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número para saber o seu fatorial: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial()
print(f'Os resultados dos fatoriais de 5, 3 e 1 são, respectivamente, {f1}, {f2}, {f3}.')

print('-' * 150)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número para saber se ele é par ou ímpar: '))
if par(num):
    print('O número é par!')
else:
    print('O número é ímpar!')

print('-' * 150)