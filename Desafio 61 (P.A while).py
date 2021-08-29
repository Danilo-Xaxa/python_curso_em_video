primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
qtd_termos = int(input('Digite a quantidade de termos da P.A: '))
termo_atual = primeiro_termo

while termo_atual != primeiro_termo + (razao * qtd_termos):
    print(termo_atual, end=' → ')
    termo_atual += razao

print('FIM')
