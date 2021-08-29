def linha():
    print('-='*55)
linha()

print('')

def mensagem(msg):
    print('-'*18)
    print(msg)
    print('-'*18)
mensagem('MENSAGEM ALEATÓRIA')

print('')

escolha = 'sim'
def texto():
    print('')
    txt = input('Quer que eu printe o quê? ').strip()
    print('')
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))
    print('')
while escolha == 'sim' or escolha == 's':
    texto()
    escolha = input('Quer continuar? [S/N] ').strip().lower()

print('')

def soma(x, y):
    print(f'X = {x} e Y = {y}.')
    s = x + y
    print(f'Soma de X e Y: {s}')
    print('')
soma(9, 7)
soma(2, 6)
soma(3234, 6353)

def contador(* num):
    tam = len(num)
    sominha = sum(num)
    print(f'No total, {tam} números foram digitados: {num}.')
    print(f'A soma deles é de {sominha}.')
    print('')
contador(2, 5, 6, 1, 7)
contador(9134010432, 13139094313)
contador(234, 641, 7523, 4654)

print('')

def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1

valores = [4, 2, 3, 6, 8, 2, 1, 7, 9, 0, 5]
dobra(valores)
print(valores)
