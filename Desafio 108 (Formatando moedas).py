from modulos_e_pacotes import modulo_moeda
n = int(input('Digite um número: '))
print(f'O dobro de {modulo_moeda.moeda(n)} é {modulo_moeda.moeda(modulo_moeda.dobrar(n))}')
print(f'Aumentando em 10%, temos {modulo_moeda.moeda(modulo_moeda.aumentar(n, 10))}')
print(f'Diminuindo em 13%, temos {modulo_moeda.moeda(modulo_moeda.diminuir(n, 13))}')
print(f'A metade de {modulo_moeda.moeda(n)} é {modulo_moeda.moeda(modulo_moeda.metade(n))}')
#o módulo tá na pasta módulos