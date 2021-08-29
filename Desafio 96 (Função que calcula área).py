def terreno():
    print('')
    print('-' * 45)
    print(' ' * 8, 'CÁLCULO DE ÁREA DE TERRENOS')
    print('-' * 45)
    comprimento = float(input('Digite o comprimento, em metros, do terreno: '))
    largura = float(input('Digite o largura, em metros, do terreno: '))
    print(f'A área de um terreno ({comprimento}x{largura}) é de {(comprimento * largura):.1f}m²')
    print('')
a = int(input('Quantas vezes você deseja printar algo? '))
for x in range(a):
    terreno()