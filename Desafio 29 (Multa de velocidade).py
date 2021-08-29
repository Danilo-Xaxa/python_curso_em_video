limite = int(input('Qual é o limite de velocidade? '))
multa_por_km = int(input('A cada quilômetro por hora além do limite, qual o valor da multa? '))
velocidade = int(input('Qual é a velocidade do carro? '))
multa_final = (velocidade - limite) * multa_por_km
if velocidade > limite:
    print(f'Você está acima do limite de velocidade. Sua multa é de {multa_final} reais.')
else:
    print('Você está dentro do limite de velocidade.')
# começando a usar o >
teste = 'teste'
print(f'\033[7;40m{teste}\033[m')
