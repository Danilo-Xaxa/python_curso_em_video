faturamento = float(input('Digite o valor do FATURAMENTO: '))
custo = float(input('Digite o valor do CUSTO: '))
ROI = ((faturamento - custo) / custo) * 100
print(f'O ROI é de {ROI:.1f}%')
