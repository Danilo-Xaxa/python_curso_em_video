salario_inicial = int(input('Qual é o valor do seu salário? '))

porcentagem = int(input('Qual é a porcentagem de aumento aplicada? '))

salario_novo = salario_inicial + (salario_inicial / (100 / porcentagem))

print(f'O valor do seu novo salário é de {salario_novo} reais.')
