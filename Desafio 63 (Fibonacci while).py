qtd_termos = int(input('Quantos termos da sequência Fibonacci você quer mostrar?: '))
primeiro_termo = 0
segundo_termo = 1

print(f'{primeiro_termo} → {segundo_termo} → ', end='')

counter = 3

while counter <= qtd_termos:
    terceiro_termo = segundo_termo + primeiro_termo
    print(f'{terceiro_termo} → ', end='')
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    counter += 1

print('FIM')
