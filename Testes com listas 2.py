dados = ['Pedro', 25]
pessoas = []
pessoas.append(dados[:])
print(pessoas[0])
print(pessoas[0][0])

print('-'*32)

teste = []
teste.append('Danilo')
teste.append(17)
galera = []
galera.append(teste[:])
teste[0] = 'Joana'
teste[1] = 19
galera.append(teste[:])
print(galera)

print('-'*32)

pessoal = [['João', 26],['Clara', 36],['Eduardo', 42],['Felipe', 21]]
for x in pessoal:
    print(f'{x[0]} tem {x[1]} anos de idade.')

print('-'*32)

q = int(input('Quantas pessoas você quer cadastrar? '))
grupo = []
dado = []
a = 0
b = 1
c = 0
for x in range(q):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:])
    dado.clear()
for x in range(q):
    print(f'{grupo[a][c]} tem {grupo[a][b]} anos de idade.')
    a += 1

print('-'*32)

a = 0
b = 1
c = 0
totalmaior = totalmenor = 0
for x in range(q):
    if grupo[a][b] >= 18:
        print(f'{grupo[a][c]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{grupo[a][c]} é menor de idade')
        totalmenor += 1
    a += 1
print(f'Total de maiores: {totalmaior}.\nTotal de menores: {totalmenor}.')