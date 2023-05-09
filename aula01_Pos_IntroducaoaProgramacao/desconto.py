#Exercício do Desconto: Escreva um programa em Python que solicite ao usuário o valor de um produto e o percentual de
#desconto. Calcule o valor do desconto e exiba o valor final após o desconto.

valor_produto = float(input('Entre com o valor do produto: '))
valor_desconto = int(input('Entre com o valor do desconto: '))

desconto = valor_produto * (valor_desconto / 100)
produto_com_desconto = (valor_produto - desconto)

print(f'O valor do produto com desconto é de: {produto_com_desconto} reais')
