from random import randint

lista_numeros = []
controle = 0

while controle < 100:
    lista_numeros.append(randint(0, 1000))
    controle += 1

print(f'Os números escolhidos são: {lista_numeros}')