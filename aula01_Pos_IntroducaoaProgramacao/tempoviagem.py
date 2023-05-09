#Exercício do Tempo de Viagem: Escreva um programa em Python que solicite ao usuário a distância de uma viagem (em
#km) e a velocidade média (em km/h). Calcule o tempo de viagem em horas e exiba o resultado.

distancia_percorrida = float(input('Entre com a distância total da viagem em km: '))
velocidade_media = float(input('Entre com a velocidade média em km/h: '))

tempo_viagem = (distancia_percorrida // velocidade_media)

print(f'Tempo estimado da viagem é de: {tempo_viagem} horas')
