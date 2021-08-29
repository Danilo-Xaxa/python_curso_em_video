dias = float(input('Diga por quantos dias o carro foi alugado: '))
km = float(input('Diga quantos quilômetros o carro andou: '))

preco = (dias * 60) + (km * 0.15)

print(f'O preço a ser pago é de R${preco:.2f}')
