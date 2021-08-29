a = input('Digite a 1ª frase: ')
c = 2
while True:
    b = input('Continuar ou parar? ').strip().upper()
    if b == 'PARAR':
        break
    a = input(f'Digite a {c}ª frase: ')
    c += 1
print('Fim')