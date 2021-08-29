sexo = input('Qual é o seu sexo? [M/F] ')

while sexo not in 'MmFf':
    sexo = input('Opção inválida, digite M ou F: ')

print('Ok, sexo registrado.')
