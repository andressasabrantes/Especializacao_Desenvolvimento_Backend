print('-----Iniciando a verificação-----')

idade = int(input('Qual a sua idade? '))
ingresso = input('Ingresso VIP ou PISTA?')
ingresso = ingresso.upper()

if idade >= 18 and ingresso == 'VIP':
    print('Você pode entrar na festa!')
    print('Siga para o primeiro andar!')
elif idade >= 18 and ingresso == 'PISTA':
    print('Você pode entrar na festa!')
    print('Siga pelo corredor!')
else:
    print('É hora de voltar para a sua casinha!')

print('-----Finalizando programa-----')
