print('''Eis as três opções de conversão:
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL''')
x = int(input('Escolha sua opção de conversão e digite-a (1, 2 ou 3): '))
a = int(input('Digite um número qualquer: '))
if x == 1:
    print(f'O resultado da conversão é {bin(a) [2:]}.')
elif x == 2:
    print(f'O resultado da conversão é {oct(a) [2:]}.')
elif x == 3:
    print(f'O resultado da conversão é {hex(a) [2:]}.')
else:
    print('Opção inválida. Reinicie e digite 1, 2 ou 3.')
#começando a usar o elif
