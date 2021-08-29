qtd_maiores = 0
qtd_homens = 0
novinhas = 0

while True:
    print('-' * 20)
    nome = input('Nome: ').strip()
    sexo = input('Sexo: [M/F] ').strip().upper()
    idade = int(input('Idade: '))

    if sexo == 'M' or sexo == 'MASCULINO' or sexo == 'MAS':
        qtd_homens += 1
    elif (sexo == 'F' or sexo == 'FEMININO' or sexo == 'FEM') and idade < 20:
        novinhas += 1

    if idade >= 18:
        qtd_maiores += 1

    print('-' * 20)

    continuar = input('Deseja continuar? [S/N] ').strip().upper()

    if continuar == 'N' or continuar == 'NÃO' or continuar == 'NAO':
        break

print('-' * 20)
print(f'{qtd_maiores} pessoas são maiores de idade.',
      f'{qtd_homens} pessoas são homens.',
      f'{novinhas} mulheres tem menos de 20 anos.', sep='\n')
