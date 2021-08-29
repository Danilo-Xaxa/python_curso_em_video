nome = input('Diga seu nome completo: ')

print(nome.upper())
print(nome.lower())

b = nome.split()

qtd_espacos = nome.count(' ')

letras_no_nome = len(nome) - qtd_espaços

print(f"Seu nome tem ao todo {letras_no_nome}")

print(len(b[0]))
