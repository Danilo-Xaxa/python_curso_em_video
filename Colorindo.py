a = input('Digite uma frase: ')
b = input('''Agora escolha uma cor!
[OPÇÕES: vermelho, azul, verde, amarelo, ciano e cinza]
Cor escolhida: ''').lower().strip()
if b == 'vermelho':
    print(f'\033[0;31m{a}\033[m')
elif b == 'azul':
    print(f'\033[0;34m{a}\033[m')
elif b == 'verde':
    print(f'\033[0;32m{a}\033[m')
elif b == 'amarelo':
    print(f'\033[0;33m{a}\033[m')
elif b == 'branco':
    print(f'\033[0;30m{a}\033[m')
elif b == 'ciano':
    print(f'\033[0;36m{a}\033[m')
elif b == 'cinza':
    print(f'\033[0;37m{a}\033[m')
else:
    print('Eita, cor inválida. Tenta de novo aí, mermão!')
