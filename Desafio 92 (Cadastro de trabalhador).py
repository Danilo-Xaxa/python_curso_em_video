dicionario = {}
dicionario['Nome'] = input('Nome: ')
data_de_nascimento = int(input('Ano de nascimento: '))
dicionario['Idade'] = 2019 - data_de_nascimento
dicionario['Carteira de trabalho'] = int(input('Carteira de trabalho (digite 0 caso não tiver): '))
if dicionario["Carteira de trabalho"] != 0:
    dicionario['Ano de contratação'] = int(input('Ano de contratação: '))
    dicionario['Salário'] = float(input('Salário: R$ '))
    dicionario['Ano de aposentadoria'] = (f'{dicionario["Ano de contratação"] + 35}')
    dicionario['Tempo para se aposentar'] = (f'{35 - (2019 - dicionario["Ano de contratação"])} anos')
    dicionario['Idade ao se aposentar'] = (f'{35 - (2019 - dicionario["Ano de contratação"]) + dicionario["Idade"]} anos')
print('')
for key, value in dicionario.items():
    print(f'{key}: {value}')