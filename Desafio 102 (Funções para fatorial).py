def fatorial(a, show=False):
    """-> CALCULA O FATORIAL DE UM NÚMERO
    :param a: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor fatorial de a"""
    numero = a
    fatorial = 1
    while numero != 1:
        fatorial *= numero
        numero = numero - 1
        if show:
            print(fatorial, end=' -> ')
    if show:
        print('FIM')
    return print(f'O fatorial de {a} é {fatorial}.')


print(fatorial(5, show=False))
#help(fatorial)