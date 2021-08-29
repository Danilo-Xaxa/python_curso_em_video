def LeiaInt(msg1):
    pronto = False
    while True:
        valor1 = input(msg1)
        if valor1.isnumeric():
            pronto = True
        else:
            print('\033[1;31mERRO! FAVOR DIGITAR UM NÚMERO INTEIRO VÁLIDO\033[m')
        if pronto:
            break
    return valor1


def linha(tamanho=42):
    return '-' * tamanho


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    x = 1
    for item in lista:
        print(f'\033[33m{x}\033[m - \033[34m{item}\033[m')
        x += 1
    print(linha())
    opç = LeiaInt('\033[32mSua opção: \033[m')
    return opç