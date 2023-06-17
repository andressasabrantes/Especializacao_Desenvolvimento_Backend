from random import randint

lista_numeros = []
for i in range(100):
    lista_numeros.append(randint(0, 1000))

print(f'A lista de números escolhidos: {lista_numeros}')