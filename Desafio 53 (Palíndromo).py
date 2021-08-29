def is_palindrome(frase):
    frase_sem_espacos = frase.lower().replace(' ', '')
    frase_reversa = ''.join(reversed(frase_sem_espacos))

    if frase_sem_espacos == frase_reversa:
        return True
    else:
        return False

frase_exemplo = input('Digite uma frase: ')

if is_palindrome(frase_exemplo):
    print('É palíndromo')
else:
    print('Não é')

'''
frase = input('Digite uma frase: ').upper().strip()

frase_splitada = frase.split()

frase_junta = ''.join(frase_splitada)

frase_inversa = ''

for counter in range(len(frase_junta) - 1, -1, -1):
    frase_inversa += frase_junta[counter]

if frase_junta == frase_inversa:
    print('É palíndromo')
else:
    print('Não é')
'''
