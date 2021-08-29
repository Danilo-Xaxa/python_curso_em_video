from random import shuffle


a = input('Diga o nome do primeiro aluno: ')
b = input('Diga o nome do segundo aluno: ')
c = input('Diga o nome do terceiro aluno: ')
d = input('Diga o nome do quarto aluno: ')

alunos = [a, b, c, d]

shuffle(alunos)

print(f'A ordem sorteada é')
print(alunos)