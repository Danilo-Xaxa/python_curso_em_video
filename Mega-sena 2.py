import random
print('-'*150)
numero = []
for u in range(6):
    r = int(input(f'Diga seu {u+1}º palpite: '))
    numero.append(r)
a = y = tentativas = 0
b = []
c = []
print('-'*60)
for z in range(6):
    while True:
        a = random.randint(1, 60)
        b.append(a)
        if (numero[y]) == b:
            break
        else:
            tentativas += 1
            b.clear()
    y += 1
    print(f'O número de tentativas para achar o {y}º resultado foi {tentativas}.')
    c.append(tentativas)
    tentativas = 0
print('-'*60)
print(f'Dessa vez, as chances eram de {(c[0])*(c[1])*(c[2])*(c[3])*(c[4])*(c[5])}.')


