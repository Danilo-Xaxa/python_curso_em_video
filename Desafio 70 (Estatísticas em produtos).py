print('-' * 30)

nome_produto = input('Nome do produto: ')
preco = float(input('Preço: '))

produto_mais_barato = nome_produto
menor_preco = preco
total_gasto = 0
produtos_mais_50 = 0

while True:
    total_gasto += preco

    if preco > 50:
        produtos_mais_50 += 1

    if preco < menor_preco:
        produto_mais_barato = nome_produto
        menor_preco = preco

    continuar = input('Deseja continuar? [S/N] ').strip().upper()

    if continuar == 'N' or continuar == 'NÃO' or continuar == 'NAO':
        break

    print('-' * 30)

    nome_produto = input('Nome: ').strip()
    preco = float(input('Preço: '))

print('=-' * 20)

print(f'''
O total gasto foi de R${total_gasto:.2f}
{produtos_mais_50} produtos custaram mais de R$50.00
O produto mais barato foi {produto_mais_barato}
''')

print('=-' * 20)
