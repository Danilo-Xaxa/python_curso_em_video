def LeiaInt(msg):
    pronto = False
    while True:
        valor = input(msg)
        if valor.isnumeric():
            pronto = True
        else:
            print('\033[1;31mERRO! FAVOR DIGITAR UM NÚMERO INTEIRO VÁLIDO\033[m')
        if pronto:
            break
    return valor


valor = LeiaInt('Digite um número: ')
print(f'Você acaba de digitar o número {valor}')

#valor vai ser a msg do LeiaInt, que é o input de ('Digite um número: ')
#pronto vai ser False
#while True, valor vai ser o input de msg
#se valor for numérico, pronto vai ser True
#se valor não for numérico, vai ser printado ERRO e pronto vai continuar sendo False
#se pronto for True, o while True sofre break
#return valor vai ser servir para não dar None quando for printar que você acaba de digitar o número valor
#fora da def, o programa vai printar que você acaba de digitar o número valor