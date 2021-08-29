while True:
    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
        c = a/b
    except:
        print('Algo deu errado...')
    else:
        print(f'O resultado é {c}')
        break
    #print('Programa encerrado!')
    finally:
        print('Programa encerrado!')
#esse comando da linha 11 não funciona, por isso o finally se faz necessário
#outros casos em que o finally é necessário é quando você usa return antes