primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
qtd_termos = int(input('Digite a quantidade de termos da P.A: '))
termo_atual = primeiro_termo
contador_while = 1
contador_termos_mostrados = 0

while contador_while <= qtd_termos:
    print(termo_atual, end=' → ')
    termo_atual += razao
    contador_while += 1
    contador_termos_mostrados += 1
print('PAUSA')

while True:
    qtd_termos_adicionais = int(input('Quantos termos você quer ver a mais? '))

    if qtd_termos_adicionais == 0:
        print(f'Programa encerrado, {contador_termos_mostrados} termos foram mostrados no total.')
        break

    for x in range(0, qtd_termos_adicionais):
        print(termo_atual, end=' → ')
        termo_atual += razao
        contador_termos_mostrados += 1
    print('PAUSA')
