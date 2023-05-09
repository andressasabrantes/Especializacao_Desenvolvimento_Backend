#Exercício do Cálculo de Área: Escreva um programa em Python que solicite ao usuário a largura e a altura de um
#retângulo. Calcule a área desse retângulo e exiba o resultado.

largura_retangulo = float(input('Entre com a largura do retângulo: '))
altura_retangulo = float(input('Entre com a altura do retângulo: '))

area = (largura_retangulo * altura_retangulo)
print(f'A área do retângulo é: {area:0.2f}')
