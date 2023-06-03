#condição para cada função da lista
# 1 - Adicionar Pessoas
# 2 - Pesquisar uma pessoa
# 3 - Listar pessoas
# 4 - Encerrar programa

lista = ['Andressa', 'Andreza', 'André', 'Auxi', 'Amanda']

while True:
    print('\n1 - Adicionar\n'
    '2 - Pesquisar\n'
    '3 - Listar pessoas\n'
    '4 - Remover pessoa\n'
    '5 - Alterar nome\n'
    '6 - Encerrar programa...')

    opcao = int(input(('\nDigite a opção desejada: ')))

    if opcao == 1:
        nome_pessoa = input('Digite o nome da pessoa que você quer adicionar: ')
        lista.append(nome_pessoa)

    elif opcao == 2:
        pesquisa_pessoa = input('Digite o nome da pessoa que você quer pesquisar: ')

        if pesquisa_pessoa in lista:
            print(f'O nome {pesquisa_pessoa} está na lista.')

        else:
            print(f'O nome {pesquisa_pessoa} não está na lista.')

    elif opcao == 3:
        for nome in lista:
            print(f' -> {nome}')

    elif opcao == 4:
        remover_pessoa = input('Qual pessoa você deseja remover? ')

        if remover_pessoa in lista:
            lista.remove(remover_pessoa)
            print(f'{remover_pessoa} foi retirado(a) da lista com sucesso!\nLista atualizada:')
            for nome in lista:
                print(f' -> {nome}')
        else:
            print('Nome não encontrado.')

    elif opcao == 5:
        nome_alterar = input('Digite o nome da pessoa que você quer alterar: ')

        if nome_alterar in lista:
            print(f'O nome {nome_alterar} foi encontrado!')
            alteracao = input('Qual será o novo nome? ')
            lista[lista.index(nome_alterar)] = alteracao
            print(f'O nome foi alterado para {alteracao} com sucesso!')

        else:
            print('O nome não foi encontrado!')

    elif opcao == 6:
        print('Encerrando programa...')
        break

    else:
        print('Entrada inválida.')
