cateto_adjacente = float(input('Diga o comprimento do cateto adjacente: '))
cateto_oposto = float(input('Diga o comprimento do cateto oposto: '))
hipotenusa = float(input('Diga o comprimento da hipotenusa: '))

seno = cateto_oposto/hipotenusa
cosseno = cateto_adjacente/hipotenusa
tangente = cateto_oposto/cateto_adjacente

print(f'O seno é {seno}, o cosseno é {cosseno} e a tangente é {tangente}')
