from time import sleep
while True:
    print('''\033[1;30;42m------------------------------------
        SISTEMA DE AJUDA PyHelp
------------------------------------
\033[m''', end='')
    comando = input('Função > ').strip().lower()
    if comando == 'fim':
        sleep(1)
        print('''\033[1;30;41m------------------------------------
        PROGRAMA ENCERRADO
------------------------------------
\033[m''')
        break
    sleep(0.5)
    print(f'''\033[1;30;44m------------------------------------
Acessando o manual do comando {comando}
------------------------------------
\033[m''')
    sleep(1)
    help(comando)
    sleep(2)