sim_nao = ''
maior = menor = media = counter = 0
lista = []

while sim_nao != 'N':
    num = int(input('Digite um número: '))
    lista.append(num)

    sim_nao = str(input('Quer continuar? [S/N] ')).upper()
    counter += 1

    media = sum(lista) / counter
    maior = sorted(lista)[-1]
    menor = sorted(lista)[0]

    if sim_nao == 'N':
        break

print(f'< Você digitou {counter} números e a média entre eles é de {media:.1f} >')
print(f'< O menor valor foi {menor} e o maior foi {maior}. A soma foi de {sum(lista)} >')
