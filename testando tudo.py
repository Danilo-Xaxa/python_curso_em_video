import modulo_uteis
numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é {modulo_uteis.fatorial(numero)}')
print(f'O dobro de {numero} é {modulo_uteis.dobro(numero)}')
print(f'O triplo de {numero} é {modulo_uteis.triplo(numero)}')

from pacote_uteis import pacote_quadruplo
from pacote_uteis import modulo_quintuplo
x = int(input('Digite um número: '))
print(f'O quadruplo de {x} é {pacote_quadruplo.quadruplo(x)}')
print(f'O quintuplo de {x} é {modulo_quintuplo.quintuplo(x)}')

import modulo_moeda
n = int(input('Digite um número: '))
print(f'O dobro de {n} é {modulo_moeda.dobrar(n)}')
print(f'Aumentando em 10%, temos {modulo_moeda.aumentar(n)}')
print(f'Diminuindo em 13%, temos {modulo_moeda.diminuir(n)}')
print(f'A metade de {n} é {modulo_moeda.metade(n)}')