a = ('Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'São Paulo', 'Athlético', 'Internacional', 'Corinthians', 'Bahia', 'Goiás')
print(f'Os times são: {a}')
print(f'Os cinco primeiros colocados do Brasileirão são: {a[0:5]}.')
print(f'Os últimos cinco colocados do Brasileirão são: {a[-5:]}.')
print(f'Ordem alfabética: {sorted(a)}.')
print(f'O Corinthians está na posição {a.index("Corinthians")}º posição.')
