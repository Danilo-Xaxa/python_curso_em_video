valores = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
valor_digitado = int(input('Digite um número entre 0 e 10: '))
while True:
    if 0 <= valor_digitado <= 10:
        print(f'Você digitou o número {valores[valor_digitado]}.')
        valor_digitado = int(input('Digite um número entre 0 e 10: '))
    else:
        print('Erro, tente novamente.')
        valor_digitado = int(input('Digite um número entre 0 e 10: '))
#começando a usar tuplas