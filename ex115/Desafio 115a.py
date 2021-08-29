from Guanabara.modulos_e_pacotes.ex115.biblioteca.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resposta == '1':
        cabeçalho('Opção 1')
    elif resposta == '2':
        cabeçalho('Opção 2')
    elif resposta == '3':
        cabeçalho('Saindo do sistema... Até logo')
        sleep(1)
        break
    else:
        print('\033[31mERRO: digite uma opção válida.\033[m')
    sleep(1)
