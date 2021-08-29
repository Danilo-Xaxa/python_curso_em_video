x = 1
par = impar = 0
while x != 0:
    x = int(input('Digite um número: '))
    if x != 0:
        if x % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')
