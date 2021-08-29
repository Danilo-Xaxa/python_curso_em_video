def leia_int(msg):
    valor = 0
    pronto = False

    while True:
        try:
            valor = int(input(msg))
            pronto = True
        except ValueError:
            print('ERRO! FAVOR DIGITAR UM NÚMERO INTEIRO VÁLIDO')

        if pronto:
            break

    return valor


def leia_float(msg):
    valor = 0
    pronto = False

    while True:
        try:
            valor = float(input(msg))
            pronto = True
        except ValueError:
            print('ERRO! FAVOR DIGITAR UM NÚMERO REAL VÁLIDO')

        if pronto:
            break

    return valor


valor_inteiro = leia_int('Digite um Inteiro: ')
valor_real = leia_float('Digite um Real: ')
print(f'O valor inteiro digitado foi {valor_inteiro} e o real foi {valor_real}')
