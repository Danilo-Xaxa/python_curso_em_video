a = str(input('Digite seu nome completo: ')).strip()
b = a.split()

print('Primeiro nome: ', (b[0]))
print('Último nome: ', (b[len(b)-1]))
