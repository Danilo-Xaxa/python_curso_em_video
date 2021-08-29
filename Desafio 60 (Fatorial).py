num = int(input('Digite um número para saber o seu fatorial: '))

antecessor = num - 1

while antecessor != 1:
    num *= antecessor
    antecessor -= 1

print(f'O fatorial do número digitado é {num}.')



'''
num = int(input('Diga um número: '))  # 5
counter = num + 1  # 6
fatorial = 1  # 1

while counter > 1:
    counter -= 1  # 5 4 3 2 1
    fatorial *= counter  # 5 20 60 120 120

print(fatorial)  # 120
'''
