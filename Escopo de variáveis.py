def teste():
    x = 6
    print(f'Na função teste, x vale {x}')
    print(f'Na função teste, n vale {n}')

n = 9
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')

#Nesse programa, 'n' é uma variável global e 'x' é uma variável local.

print('')

def outroteste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'O "a" de dentro vale {a}')
    print(f'O "b" de dentro vale {b}')
    print(f'O "a" de dentro vale {c}')

a = 5
outroteste(a)
print(f'O "c" de fora vale {a}')

#Nesse programa, temos dois "a", um "a" global (que é o "a" de fora, que vale 5) e "a" um local (que é o "a" de dentro, que vale 8)
#Porém, se você quiser tornar o "a" de dentro global, escreva global a

#Esse assunto se chama escopo de variáveis. Como dito, existe o escopo global e o escopo local