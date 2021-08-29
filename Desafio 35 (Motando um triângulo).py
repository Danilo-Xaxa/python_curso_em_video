a = float(input('Diga a medida do primeiro lado do triângulo: '))
b = float(input('Diga a medida do segundo lado do triângulo: '))
c = float(input('Diga a medida do terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < b + a:
    print('Certo, é possível montar um triângulo com essas medidas.')
else:
    print('Não é possível montar um triângulo com tais medidas.')