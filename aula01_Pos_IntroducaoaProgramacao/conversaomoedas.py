#Exercício da Conversão de Moedas: Escreva um programa em Python que solicite ao usuário um valor em Real (BRL) e
#faça a conversão desse valor para Dólar Americano (USD). Considere a taxa de câmbio fixa de 1 USD = 5 BRL. Exiba o
#valor convertido na tela.

real = float(input('Qual valor você deseja converter? '))
taxa_cambio = float(input('Qual a taxa de câmbio de hoje? '))

valor_dolar = (real / taxa_cambio)
print(f'Você tem {valor_dolar} dólares')
