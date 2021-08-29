print('\033[1;34m-\033[m-'*150)
print(' '*27, '\033[1;32mBEM-VINDO AO SIMULADOR DE INVESTIMENTOS DE RENDA FIXA DA DX CORRETORA\033[m')
print('\033[1;34m-\033[m-'*150)
print('''
Escolha um dos seguintes investimentos:
[A] Poupança
[B] CDB do Banco Inter (100% do CDI)
[C] LCI/LCA
[D] Tesouro Selic
[E] Outro (escolher taxa)''')
escolha = input('Sua escolha: ').strip().lower()
print('')
aporte_inicial = int(input('Aporte inicial: R$ '))
aporte_mensal = int(input('Aporte mensal: R$ '))
if escolha == 'a' or escolha == 'poupança':
    taxa = 0.29
elif escolha == 'b' or escolha == 'cdb' or escolha == 'cdb do inter' or escolha == 'inter' or escolha == 'cdi' or escolha == '100% do cdi':
    taxa = 0.37
elif escolha == 'c' or escolha == 'lci' or escolha == 'lca' or escolha == 'lci/lca':
    taxa = 0.4
elif escolha == 'd' or escolha == 'tesouro' or escolha == 'selic' or escolha == 'tesouro selic':
    taxa = 0.38
elif escolha == 'e' or escolha == 'outro' or escolha == 'escolher' or escolha == 'escolher taxa' or escolha == 'escolher a taxa' or escolha == 'outro (escolher taxa)' or escolha == 'outro (escolher a taxa)':
    taxa = float(input('Taxa mensal (porcentagem): '))
tempo = int(input('Tempo (meses): '))
total_investido = aporte_inicial + (aporte_mensal * tempo)
total_bruto = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))
total_gerado = total_bruto - total_investido
print('')
print(f'Total investido: R$ {total_investido}')
print(f'Dinheiro gerado pelo investimento: R$ {total_gerado:.2f}')
print(f'Total bruto: R${total_bruto:.2f}')