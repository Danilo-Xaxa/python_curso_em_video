dados = {'nome': 'Danilo', 'idade': '17'}
print(dados['nome'])

print('')

SW = {'título': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
for key, value in SW.items():
    print(f'O {key} é {value}')

print('')

muse = {'guitarrista': 'Matt', 'baixista': 'Chris', 'bateirista': 'Dom'}
print(muse.items())
print(muse.values())
print(muse.keys())

print('')

estado = {}
brasil = []
for c in range(3):
    estado['nome'] = input('Digite o nome do estado: ')
    estado['sigla'] = input('Digite a sigla do estado: ')
    brasil.append(estado.copy())
    print(f'A sigla do estado {brasil[c]["nome"]} é {brasil[c]["sigla"]}.')
    print('-' * 30)
