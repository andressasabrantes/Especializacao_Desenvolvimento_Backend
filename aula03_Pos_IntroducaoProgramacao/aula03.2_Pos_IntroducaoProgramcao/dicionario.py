professor = {
    'nome': 'Messias',
    'idade': 36
}

aluno = {
    'nome': 'Aluno 1',
    'idade': 123
}

print(professor['nome'])
print(aluno['nome'])

professores = {
    'Messias': {
        'idade': 36,
        'Disciplinas': ['Introdução', 'Java']},
    'Wuldson': {
        'idade': 53,
        'Disciplinas': ['BD I', 'BD II']}
}

print(professores['Messias'])
print(professores['Wuldson'])

#Acessando valores
print(f'O professor Messias tem {professores["Messias"]["idade"]} anos, e ministra as disciplinas de {professores["Messias"]["Disciplinas"]}')

#Adicionando novas chaves e valores
professores['Messias']['Email'] = 'mrafael@gmail.com'
professores['Messias']['Cpf'] = '000.000.000-00'
professores['Messias']['Endereço'] = {
    'Rua': 'Central',
    'Número': 123,
    'Bairro': 'Intermares'
}
print(f'O email do professor Messias é: {professores["Messias"]["Email"]}')
print(f'O cpf do professor Messias é: {professores["Messias"]["Cpf"]}')
print(f'O bairro do professor Messias é: {professores["Messias"]["Endereço"]["Bairro"]}')


#Adicionando novas chaves e valores
professores['Wuldson']['Email'] = 'professorwuldson@gmail.com'
professores['Wuldson']['Cpf'] = '000.000.000-00'
print(f'O email do professor Wuldson é: {professores["Wuldson"]["Email"]}')
print(f'O cpf do professor Wuldson é: {professores["Wuldson"]["Cpf"]}')

#Deletando o cpf
del professores['Messias']['Cpf']
print(professores["Messias"])

