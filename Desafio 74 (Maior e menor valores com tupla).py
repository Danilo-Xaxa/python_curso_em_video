import random
random = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'Os números sorteados são: {random}')
#printa os numeros sorteados
organizador = sorted(random)
#organiza os numeros sorteados
print(f'O maior número é {organizador[4]} e o menor é {organizador[0]}.')
#