idade_mais_velho = 0
soma_idades = 0
mais_velho = ''
contador_novinhas = 0

for counter in range(1, 5):
    print(f'-- Pessoa {counter} --')

    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    soma_idades += idade

    if idade > idade_mais_velho and sexo == 'M':
        idade_mais_velho = idade
        mais_velho = nome

    if idade < 20 and sexo == 'F':
        contador_novinhas += 1

media_idades = soma_idades / 4

print(f'A média da idade do grupo é {media_idades} anos')
print(f'O homem mais velho tem {idade_mais_velho} anos e seu nome é {mais_velho.capitalize()}')
print(f'Ao todo são {contador_novinhas} novinhas')
