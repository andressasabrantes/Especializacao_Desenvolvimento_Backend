#ler todas as linhas do arquivo

file_01 = 'contos_dos_irmaos_grimm.txt'
file_02 = 'o_principe_maquiavel.txt'

with open(file_01, 'r', encoding='utf-8') as object_file1, open(file_02, 'r', encoding='utf-8') as object_file2:
    count_line1 = 0
    for linha in object_file1:
        count_line1 += 1
        print(linha)

    count_line2 = 0
    for linha in object_file2:
        count_line2 += 1
        print(linha)

print(f'Count do livro 1: {count_line2}')
print(f'Count do livro 2: {count_line1}')