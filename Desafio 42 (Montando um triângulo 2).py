primeiro = float(input('Diga a medida do primeiro lado do triângulo: '))
segundo = float(input('Diga a medida do segundo lado do triângulo: '))
terceiro = float(input('Diga a medida do terceiro lado do triângulo: '))

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    if primeiro == segundo and segundo == terceiro:
        print('Triangulo equilátero')
    elif primeiro == segundo or primeiro == terceiro:
        print('Triangulo isóceles')
    else:  # ou elif primeiro != segundo and primeiro != terceiro and segundo != terceiro:
        print('Triangulo escaleno')
else:
        print('Não é possível montar um triângulo com tais medidas.')
