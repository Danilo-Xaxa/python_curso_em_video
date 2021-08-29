nome = input('Qual seu nome? ').strip().capitalize()
idade = input('Qual sua idade? ').strip()
cor = input('Qual sua cor favorita? ').strip().lower()
if cor == 'vermelho':
    print(f'\033[0;31m{nome}, {idade}\033[m')
elif cor == 'azul':
    print(f'\033[0;34m{nome}, {idade}\033[m')
elif cor == 'verde':
    print(f'\033[0;32m{nome}, {idade}\033[m')
elif cor == 'amarelo':
    print(f'\033[0;33m{nome}, {idade}\033[m')
elif cor == 'branco':
    print(f'\033[0;30m{nome}, {idade}\033[m')
elif cor == 'ciano':
    print(f'\033[0;36m{nome}, {idade}\033[m')
elif cor == 'cinza':
    print(f'\033[0;37m{nome}, {idade}\033[m')
else:
    print('Eita, cor inválida. Tenta de novo aí, mermão!')
