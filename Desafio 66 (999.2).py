cont = soma = 0

while True:
    num = int(input('Digite um número. [999 para encerrar]: '))

    if num == 999:
        break

    cont += 1
    soma += num

print(f'Programa encerrado, você inseriu {cont} números e a soma deles é de {soma}.')
