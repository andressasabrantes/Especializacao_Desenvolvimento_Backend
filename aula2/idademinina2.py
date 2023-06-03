print('-----Iniciando a verificação-----')

idade = int(input('Qual a sua idade? '))

if idade < 18:
    print('Pode ir pra casa!')
else:
    ingresso = input('Ingresso VIP ou PISTA?')
    ingresso = ingresso.upper()

    if ingresso == 'VIP':
        print('Você pode entrar na festa!')
        print('Siga para o primeiro andar!')
    elif ingresso == 'PISTA':
        print('Siga para a pista!')
    else:
        print('É hora de voltar para a su casinha!')

print('-----Finalizando programa-----')
