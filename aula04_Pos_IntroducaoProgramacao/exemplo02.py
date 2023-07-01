diretorio = 'teste\\'
arquivo = 'arquivo2.txt'
file_path = diretorio + arquivo

with open(file_path, 'r') as file_object:
    conteudo = file_object.read()
    print(conteudo)