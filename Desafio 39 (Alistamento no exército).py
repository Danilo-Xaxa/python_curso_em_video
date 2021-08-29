from datetime import date


data_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - data_nascimento

print(f'Quem nasceu em {data_nascimento} tem {idade} anos em 2021')

if idade < 18:
    resta = 18 - idade
    print(f'Ainda faltam {resta} anos para o alistamento')
    print(f'Seu alistamento será em {ano_atual + resta}')
else:
    print('EAE BORA SE ALISTAR KKKKKKKKKKKKKKKKKK TOMOU NO CU')
