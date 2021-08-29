subtotal = 0
escolha = mais = 'sim'
while escolha != 'não' and escolha != 'nao' and escolha != 'n':
    valor = float(input('Preço: ').strip())
    subtotal += (valor * (float(input('Quantidade: ').strip())))
    print(f'Subtotal: {subtotal:.1f}')
    escolha = input('Continuar? [S/N] ').strip().lower()
    print('-' * 40)
ProdutosNoPeso = [['MAÇÃ', 8.6], ['PÊRA', 10.10], ['GOIABA', 5.6],
                  ['LARANJA', 3.5], ['LIMÃO', 4.6], ['MACAXEIRA', 2.5],
                  ['CARÁ', 5.6], ['BATATA', 4.2], ['BATATA DOCE', 3.8],
                  ['PEPINO', 3], ['CENOURA', 3], ['CEBOLA', 2.5],
                  ['TOMATE', 3], ['ALHO', 22.4], ['BANANA', 3.5]]
for x in range(len(ProdutosNoPeso)):
    subtotal += (float(input(f'Quantos quilos de {ProdutosNoPeso[x][0]}? ').strip()) * ProdutosNoPeso[x][1])
    print(f'Subtotal: {subtotal:.1f}')
    print('-' * 40)
mais = input('Quer mais algum produto no peso? ').strip().lower()
if mais == 'sim' or mais == 's':
    while mais == 'sim' or mais == 's':
        nome = input('Nome do produto: ')
        quilos = float(input(f'Quantos quilos de {nome}? '))
        valor = float(input(f'Qual é o preço do quilo de {nome}? '))
        subtotal += (quilos * valor)
        print(f'Subtotal: {subtotal:.1f}')
        print('-' * 40)
        mais = input('Quer mais algum produto no peso? ').strip().lower()
print('-' * 40)
print(f'TOTAL: R$ {subtotal:.2f}')
#posso também criar a funcionalidade de gerar uma nota fiscal com todos os produtos, quantidade/peso e preço por unidade/quilo
#posso também criar a fucnionalidade de conferir se o preço do quilo dos alimentos são realmente aqueles declarados