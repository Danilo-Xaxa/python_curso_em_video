# Criando a listona e a lista de molieres
listona, molieres = [], []

# Iniciando a variável de soma das idades
soma_idades = 0

while True:
    #Pegando o nome
    nome = input('Digite o nome: ')

    # Pegando o sexo (e insistindo se a pessoa não digitar corretamente)
    sexo = input('Digite o sexo: ').upper()
    while sexo not in ['M', 'F']:
        sexo = input('Erro! Digite M ou F: ').upper()

    # Se for o sexo for 'F', adiciona o nome na lista de molieres
    if sexo == 'F':
        molieres.append(nome)

    # Pegando a idade
    idade = int(input('Digite a idade: '))

    # Criando o dicionário e colocando ele dentro da listona
    dicio = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    listona.append(dicio)

    # Aumentando a soma das idades
    soma_idades += idade

    # Ver se o usuário quer continuar (e insistindo se a pessoa não digitar corretamente)
    s_n = input('Quer continuar? [S/N] ').upper()
    while s_n not in ['S', 'N']:
        s_n = input('Erro. Digite S ou N: ').upper()

    # Se a resposta for 'N', 'NAO' ou 'NÃO', dá um break
    if s_n in ['N', 'NAO', 'NÃO']:
        break

print('-=' * 20)

media = soma_idades / len(listona)  # Calculando a média de idades

print(f'A) Ao todo temos {len(listona)} pessoas cadastradas')
print(f'B) A média de idade é de {media}')
print(f'C) As molieres cadastradas foram: {molieres}')

print(f'D) Lista das pessoas que estão acima da média: ')
for dicio in listona:  # Para cada dicionário dentro da listona
    if dicio['Idade'] > media:  # Se a idade da pessoa for maior que a média de idade
        print(f"NOME: {dicio['Nome']}, SEXO: {dicio['Sexo']}, IDADE: {dicio['Idade']}")  # Printar nome, sexo e idade da pessoa
