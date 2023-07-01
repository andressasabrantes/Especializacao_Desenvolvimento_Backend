print('--- Iniciando o programa ---')
op = input('Digite 0 para ver as pessoas que não têm permissão e 1 para as pessoas que têm permissão: ')

with open('teste\\arquivo3.txt', 'r') as object_file:
    for linha in object_file:
        if linha[0] == op:
            print(linha.rstrip())