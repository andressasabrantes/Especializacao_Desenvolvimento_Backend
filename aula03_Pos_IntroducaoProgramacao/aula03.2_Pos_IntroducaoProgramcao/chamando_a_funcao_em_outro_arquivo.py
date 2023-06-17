import funcoes_soma_subtracao
from random import randint

while True:
    op = input('Digite a opção: \n'
               '1 - Somar\n'
               '2 - Subtrair\n'
               '3 - Sair')
    op = int(op)

    match op:
        case 1:
            resultado = funcoes_soma_subtracao.soma(
                randint(1, 5), randint(1, 5))
            print(f'A soma foi: {resultado}')
        case 2:
            resultado = funcoes_soma_subtracao.subtrair(
                randint(100, 200), randint(100, 200))
            print(f'A subtração foi de: {resultado}')
        case 3:
            print('Encerrando programa...')
            break
        case _:
            print(f'Opção inválida!')


