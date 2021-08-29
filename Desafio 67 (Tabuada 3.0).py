while True:
    multiplicador = 1
    print('-'*45)
    num = int(input('Digite um número para saber sua tabuada: '))

    if num < 0:
        break

    while multiplicador <= 10:
        print(f'{num} x {multiplicador} = {num * multiplicador}')
        multiplicador += 1

print('*O VALOR DIGITADO É NEGATIVO*')
