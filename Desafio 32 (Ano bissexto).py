a = int(input('Diga um ano entre 2000 e 2019. Eu direi se o ano é bissexto ou não: '))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é bissexto. ')
else:
    print(f'O ano {a} não é bissexto. ')
