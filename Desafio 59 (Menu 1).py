print('Olá, tudo bem? Este é o Menu 1.')

print('')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print('')

opcao = 0

while opcao != 5:
    print('---------------------------------------')

    opcao = int(input('''
O que você quer fazer?
[1] Somar
[2] Multiplicar
[3] Saber qual é o maior
[4] Inserir outros números
[5] Encerrar o programa

Opção escolhida: '''))

    if opcao == 1:
        print(f'*A soma entre {num1} e {num2} é {num1 + num2}*')
    elif opcao == 2:
        print(f'*O produto de {num1} e {num2} é {num1 * num2}*')
    elif opcao == 3:
        if num1 > num2:
            print(f'*O maior número é {num1}*')
        elif num1 == num2:
            print('*Os dois números são iguais*')
        else:
            print(f'*O maior número é {num2}*')
    elif opcao == 4:
        num1 = int(input('Insira um novo número: '))
        num2 = int(input('Insira outro novo número: '))
    elif opcao not in [1, 2, 3, 4, 5]:
        print('Erro, essa opção é inválida. Tente novamente!')

print('')

print('Programa encerrado com sucesso.')
