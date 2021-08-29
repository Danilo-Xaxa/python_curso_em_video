# Importando random.randint
from random import randint


# Função que adciona 5 números aleatórios dentro da lista
def sorteia(nums):
    for _ in range(5):
        nums.append(randint(1, 10))
    print('Nova lista (com números sorteados):', nums)


# Função que soma os números pares
def soma_pares(nums):
    soma = 0
    for num in nums:
        if num % 2 == 0:
            soma += num
    print('Soma de todos os valores pares:', soma)


# Lista de números vazia
numeros = []

# Chamando a função que sorteia
sorteia(numeros)

# Chamando a função que soma os números pares
soma_pares(numeros)
