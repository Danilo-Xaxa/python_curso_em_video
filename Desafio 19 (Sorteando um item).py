from random import choice


a = input('Diga o nome do primeiro aluno: ')
b = input('Diga o nome do segundo aluno: ')
c = input('Diga o nome do terceiro aluno: ')
d = input('Diga o nome do quarto aluno: ')

alunos = [a, b, c, d]
sorteado = choice(alunos)

print(f'O aluno sorteado é {sorteado}')
