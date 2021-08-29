def printada():
    print('')
    txt = input('Quer que eu printe o quê? ').strip()
    print('')
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))
    print('')
a = int(input('Quantas vezes você deseja printar algo? '))
for x in range(a):
    printada()