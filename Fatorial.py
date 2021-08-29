numero = int(input('Digite o número desejado: '))
fatorial = 1
while numero != 1:
    fatorial *= numero
    numero = numero - 1
    print(fatorial, end=' -> ')
print('FIM')
print(f'O fatorial é {fatorial}')