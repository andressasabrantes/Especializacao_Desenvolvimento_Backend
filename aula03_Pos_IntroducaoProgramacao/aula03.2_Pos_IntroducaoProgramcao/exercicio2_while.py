meu_nome = 'Andressa'

print('Digite o meu nome: ')
meu_nome = input()

while meu_nome != 'Andressa' and meu_nome != 'andressa':
    print('Nome errado! Digite novamente...')
    meu_nome = input()

print('Parabéns!Você acertou!')


while True:
    guess = input('Digite seu nome: ').upper()
    nome = 'seu nome'.upper()
    if guess == nome:
        print('Parabéns, você acertou!')
        break;
    else:
        print('Não foi dessa vez! Tente novamente...')




