print('---Calculando o seu peso ideal---')
genero_usuario = input('Qual o seu sexo? M ou F: ').upper()
altura = float(input('Qual a sua altura? '))

if genero_usuario == 'M':
    peso_ideal = (72.7 * altura) - 58
elif genero_usuario == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print('Entrada inválida!')

print(f'Você que é do gênero {genero_usuario}, tem peso ideal de {peso_ideal}!')
print('---Encerrando programa---')

