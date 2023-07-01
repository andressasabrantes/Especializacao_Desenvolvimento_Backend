file = 'arquivo.txt'

with open(file, 'r') as file_object:
    for linha in file_object:
        print(linha)