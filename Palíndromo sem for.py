import unidecode
a = str(input('Digite uma frase qualquer: ')).strip().upper()
a2 = unidecode.unidecode(a)
b = a2.split()
c = ''.join(b)
d = c[::-1]
print(f'A frase *{c}* ao contrário fica *{d}*')
if c == d:
    print('Isto é um palíndromo!')
else:
    print('Isto não é um palíndromo.')