from biblioteca.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resposta == '1':
        #Opção de listar o conteúdo de um arquivo
        LerArquivo(arq)
    elif resposta == '2':
        #Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == '3':
        #Opção de sair do sistema
        cabeçalho('Saindo do sistema... Até logo')
        sleep(1)
        break
    else:
        print('\033[31mERRO: digite uma opção válida.\033[m')
    sleep(2)

