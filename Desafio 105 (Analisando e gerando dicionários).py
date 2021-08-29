def notas(*num, Sit):
    """-> Analisa a nota e situação de um aluno
    :param num: uma ou mais notas do aluno (aceita várias)
    :param sit: opcional, indica se deve ou não mostrar a situação do aluno
    :return: dicionário com as notas (e talvez a situação) do aluno"""
    resultado = {'Total': len(num), 'Maior': max(num), 'Menor': min(num), 'Média': (sum(num)/(len(num)))}
    if Sit:
        if resultado['Média'] >= 7:
            resultado['Sit'] = 'APROVADO'
        else:
            resultado['Sit'] = 'REPROVADO'
    return resultado

x = notas(5.5, 9.5, 10, 6.5, Sit=True)
print(x)
help(notas)