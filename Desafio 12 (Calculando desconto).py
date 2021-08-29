preço = int(input('Qual é o preço do produto? '))

porcentagem_de_desconto = int(input('Qual é a porcentagem de desconto aplicada? '))

novo_preço = (preço - (preço / (100 / porcentagem_de_desconto)))

print(f'O preço do produto com desconto é {novo_preço}.')
