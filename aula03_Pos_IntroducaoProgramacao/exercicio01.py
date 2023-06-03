#Declarando uma lista em Python

nomes = ['Messias', 'Verônica', 'Miguel', 'Gabriela']

print(nomes)
print(f'O tipo de dado é: {type(nomes)}')

print(f'Imprimindo a posição 0 -> {nomes[0]}')
print(f'Imprimindo a posição 1 -> {nomes[1]}')
print(f'Imprimindo a posição 2 -> {nomes[2]}')
print(f'Imprimindo a posição 3 -> {nomes[3]}')

frutas = ['pêra', 'uva', 'maçã', 'kiwi']
print(frutas)
frutas[1] = 'abacate'
print(frutas)

frutas.insert(2, 'morango')
frutas.insert(4, 'graviola')
frutas.insert(1, 'pitanga')

print(frutas)

del frutas[1]
print(frutas)
del frutas[4]
print(frutas)

frutas.insert(5, 'melancia')
indice_melancia = frutas.index('melancia')
print(indice_melancia)
print(frutas)
del frutas[indice_melancia]
print(frutas)

frutas.remove('kiwi')
print(frutas)

print(f'O tamanho da lista é: {len(frutas)}')

frutas.insert(2, 'Abacaxi')
print(frutas)
indice_abacaxi = frutas.index('Abacaxi')
abacaxi_pop = frutas.pop(indice_abacaxi)
print(frutas)
print(f'A fruta deletada foi: {abacaxi_pop}')
