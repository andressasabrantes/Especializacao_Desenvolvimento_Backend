with open('arquivo.txt', 'r') as file_object:
    conteudo = file_object.read()
    print(f'Tipo: {type(conteudo)} \n{conteudo}')