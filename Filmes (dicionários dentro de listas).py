locadora = []
x = 'sim'
while x == 'sim' or x == 's':
    print('-' * 30)
    filme = {}
    filme['titulo'] = input('Título do filme: ')
    filme['ano'] = input('Ano do filme: ')
    filme['diretor'] = input('Diretor do filme: ')
    locadora.append(filme)
    x = input('Quer continuar? [S/N] ').strip().lower()
print('-' * 30)
for y in range(len(locadora)):
    print(f'{locadora[y]["titulo"]} é um filme de {locadora[y]["ano"]} dirigido por {locadora[y]["diretor"]}')