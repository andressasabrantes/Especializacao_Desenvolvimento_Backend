print('Vamos descobrir se você já pode votar e tirar habilitação!')

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2023
idade = (ano_atual - ano_nascimento)

print(f'Você tem {idade} anos!')

if idade >= 16 and idade < 18:
    print(f'Você já tem idade para votar, mas ainda não pode tirar habilitação!')
elif idade >= 18:
    print(f'E já pode tirar sua habilitação e votar!')
else:
    print('Você ainda não pode votar e tirar uma habilitação!')
