from modulos_e_pacotes import modulo_moeda2
n = int(input('Digite um número: '))
print(f'O dobro de {modulo_moeda2.monetario(n)} é {modulo_moeda2.dobrar(n, True)}')
print(f'Aumentando em 10%, temos {modulo_moeda2.aumentar(n, 10, True)}')
print(f'Diminuindo em 13%, temos {modulo_moeda2.diminuir(n, 13, True)}')
print(f'A metade de {modulo_moeda2.monetario(n)} é {modulo_moeda2.metade(n, True)}')
#o módulo tá na pasta módulos