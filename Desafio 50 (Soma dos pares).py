numeros = []

for counter in range(1, 7):
    numeros.append(int(input(f'Diga o {counter}° numero: ')))

resultado = 0

for num in numeros:  # pra cada item da lista "numeros"
    if num % 2 == 0:  # se o número é par
        resultado += num  # o resultado irá adicionar o num

print(f'Resultado é: {resultado}')
