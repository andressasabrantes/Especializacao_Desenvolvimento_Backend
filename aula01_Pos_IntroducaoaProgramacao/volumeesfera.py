import math

#Exercício do Volume de uma Esfera: Escreva um programa em Python que solicite ao usuário o raio de uma esfera.
#Calcule o volume dessa esfera usando a fórmula V = (4/3) * pi * r³, onde pi é uma constante aproximada de 3.1415. Exiba
#o volume calculado na tela.

raio_esfera = float(input('Qual o valor do raio da esfera? '))

volume_esfera = (4 / 3) * math.pi * (raio_esfera ** 3)

print(f'O volume da esfera é {volume_esfera}')
