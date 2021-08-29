altura = float(input('Diga a altura, em metros, da sua parede: '))
comprimento = float(input('Diga o comprimento, em metros, da sua parede: '))

area = altura * comprimento
litros = area / 2

print('Você precisa de', litros, 'litros de tinta para pintar a sua parede')
