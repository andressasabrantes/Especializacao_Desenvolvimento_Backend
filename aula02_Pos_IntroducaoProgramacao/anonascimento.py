print('Você já pode votar?')

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2023

if ano_nascimento >= 2007 and ano_nascimento < 2005:
    idade = ano_nascimento - ano_atual
elif ano_nascimento >= 2005:
    idade = ano_nascimento - ano_atual

print(f'Você tem ')


