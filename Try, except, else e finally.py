try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    c = a/b
except:
    print('Algo deu errado...')
else:
    print(f'O resultado é {c}')
    #esse else não é desnecessário pois, se eu printasse que o resultado é c lá dentro do try, não ia funcionar
finally:
    print('Programa encerrado!')