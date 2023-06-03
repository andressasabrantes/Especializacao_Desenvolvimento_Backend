print("Iniciando o cálculo da média: ")
nota1 = float(input("Qual a sua nota 1?"))
nota2 = float(input("Qual a sua nota 2?"))
nota3 = float(input("Qual a sua nota 3?"))
nota4 = float(input("Qual a sua nota 4?"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print('Sua média é: ', media)
    print('Você está aprovado!')
else:
    print('Sua média é: ', media)
    print('Você ainda não foi aprovado!Tente novamente próximo ano!')
