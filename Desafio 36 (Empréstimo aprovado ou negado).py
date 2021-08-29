valor = int(input('Quanto custa a casa? '))
salario = int(input('Qual é o salário do seu comprador? '))
anos = int(input('Em quantos anos o comprador irá pagar a casa? '))

meses = anos * 12
prestacao = valor / meses

print(f'O valor da prestação mensal é de {prestacao:.2f} reais.')

if prestacao < salario / 100 * 30:
    print(f'Seu empréstimo foi aprovado. Pois esse valor de {prestacao:.2f} corresponde a MENOS de 30% do salário do comprador.')
else:
    print(f'Seu empréstimo foi negado. Pois esse valor de {prestacao:.2f} corresponde a MAIS de 30% do salário do comprador.')
