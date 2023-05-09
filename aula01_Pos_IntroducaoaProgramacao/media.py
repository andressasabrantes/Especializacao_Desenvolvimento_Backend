#Exercício da Média: Escreva um programa em Python que solicite ao usuário duas notas e calcule a média entre elas. Em
#seguida, exiba o resultado na tela.

#Recebendo os inputs dos usuários
nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))

#Calculando a média do usuário
media = (nota_1 + nota_2) / 2

#Imprimindo a média
print(f'Sua média é: {media}')
