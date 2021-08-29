atual_maior = 0
atual_menor = 0

for counter in range(1, 6):
    peso = float(input(f'Peso da {counter}° pessoa: '))
    atual_menor = peso

    if peso > atual_maior:
        atual_maior = peso
    elif peso < atual_menor:
        atual_menor = peso

print(atual_menor, atual_maior)
