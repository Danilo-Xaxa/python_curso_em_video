num = int(input('Digite um número: '))

qtd_divisores = 0

for counter in range(1, num + 1):  # de 1 a num
    if num % counter == 0:  # se num pode ser divido por counter sem sobrar nada (0)
        qtd_divisores += 1  # mais um divisor

if qtd_divisores == 2:
    print('É primo')
else:
    print('Não é')

# numero primo é um número que só pode ser dividido (sem resto nenhum) por 1 e por ele mesmo. Exemplos: 1, 2, 3, 5, 7...

# numero primo só tem 2 (divisores) que é a quantidade mínima de divisores que um número pode ter

# esse programa tem que contar o número de divisores de num. se for 2, ele é número primo. se for mais de 2, não é
