idade = int(input('Olá, atleta. Qual é a sua idade? '))

if idade < 9:
    print('Você é um atleta mirim.')
elif idade < 14:
    print('Você é um atleta infantil.')
elif idade < 19:
    print('Você é um atleta júnior.')
elif idade < 20:
    print('Você é um atleta sênior.')
else:
    print('Você é um atleta master.')
