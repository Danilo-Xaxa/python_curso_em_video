aluno = {}
aluno['nome'] = input('Qual é o nome do aluno? ')
aluno['nota'] = float(input(f'Qual é a média de {aluno["nome"]}? '))
if aluno['nota'] >= 7:
    print(f'O aluno {aluno["nome"]}, que teve a média {aluno["nota"]}, está aprovado.')
else:
    print(f'O aluno {aluno["nome"]}, que teve a média {aluno["nota"]}, está reprovado.')