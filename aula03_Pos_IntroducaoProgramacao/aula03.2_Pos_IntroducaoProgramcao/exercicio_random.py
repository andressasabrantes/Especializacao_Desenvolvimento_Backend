from random import randint

lista_numeros = []
controle = 0

while controle < 100:
    lista_numeros.append(randint(0, 1000))
    controle += 1

print(f'Os números escolhidos são: {lista_numeros}')

lista_pares = []
n_par = 0
lista_impares = []
n_impar = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
        n_par += 1
    else:
        lista_impares.append(numero)
        n_impar += 1

print(f'A lista de pares: {lista_pares} e foram: {n_par} números pares')
print(f'A lista de impares: {lista_impares} e foram: {n_impar} números impares')