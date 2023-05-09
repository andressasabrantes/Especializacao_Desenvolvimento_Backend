# Exercício do IMC (Índice de Massa Corporal): Escreva um programa em Python que solicite ao usuário sua altura em
#metros e seu peso em quilogramas. Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura *
#altura). Exiba o resultado do IMC na tela.

altura_usuario = float(input('Entre com a sua altura: '))
peso_usuario = float(input('Entre com o seu peso: '))

imc = peso_usuario / (altura_usuario * altura_usuario)

print(f'Seu IMC é aproximadamente: {imc:0.2f}')
