frase = input('Digite uma frase: ').lower().strip()

print(f'A letra "a" aparece {frase.count("a")} vezes na frase.')
print(f'A primeira letra "a" da frase aparece na posição {frase.find("a")}.')
print(f'A última letra "a" da frase aparece na posição {frase.rfind("a")}.')
