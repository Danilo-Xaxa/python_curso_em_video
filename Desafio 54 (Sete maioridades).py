from datetime import date


menores = 0

for x in range(1, 8):
    pessoa = int(input(f'Digite o ano de nascimento da {x}ª pessoa: '))
    if date.today().year - pessoa < 21:
        menores += 1

print(f'{7 - menores} são maiores e {menores} são menores.')
