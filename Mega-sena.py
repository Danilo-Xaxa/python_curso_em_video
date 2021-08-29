import random
print('-'*150)
numero = [[random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)]]
for x in range(6):
    print(f'O {x+1}º número é: {numero[x]}')
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
print(f'Multiplicando tais valores, temos o resultado de: {(c[0])*(c[1])*(c[2])*(c[3])*(c[4])*(c[5])}.')


