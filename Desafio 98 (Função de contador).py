def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
    if fim > inicio:
        while fim >= inicio:
            print(inicio, '→ ', end='')
            inicio += passo
    elif inicio > fim:
        while inicio >= fim:
            print(inicio, '→ ', end='')
            inicio -= passo
    print('Fim')
    print('')
contador(1, 10, 1)
contador(10, 0, 2)
print('-HORA DE FAZER SUAS CONTAGENS PERSONALIZADAS-')
while True:
    a = int(input('Digite o número de início: '))
    b = int(input('Digite o número fim: '))
    c = int(input('Digite o número do passo: '))
    print('')
    contador(a, b, c)