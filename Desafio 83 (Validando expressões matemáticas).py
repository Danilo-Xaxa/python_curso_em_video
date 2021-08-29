ponto = 0
a = str(input('Digite uma expressão matemática que use parênteses: '))
print('')
if a.count('(') == a.count(')'):
    print('A expressão tem um número igual de parênteses.')
    ponto += 1
else:
    print('A expressão tem um número desigual de parênteses.')
if a[len(a)-1] is ')':
    print('A expressão termina fechando parênteses.')
    ponto += 1
else:
    print('A expressão não termina fechando parênteses.')
if ponto == 2:
    print('A expressão faz uso adequado dos parânteses.')
else:
    print('A expressão não faz uso adequado dos parânteses.')
