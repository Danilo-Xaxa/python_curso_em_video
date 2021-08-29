num = 0
qtd_num = 0
soma = 0

while num != 999:
    num = int(input('Digite um número. [999 para encerrar]: '))
    qtd_num += 1
    soma += num

print(f'Programa encerrado, você inseriu {qtd_num - 1} números e a soma deles é de {soma - 999}.')
