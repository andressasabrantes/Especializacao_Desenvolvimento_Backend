import math

altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digit o raio do cilindro: '))
comprimento = (2 * math.pi * raio * altura)

area_lateral = (2 * math.pi * raio * altura)
area_base = math.pi * (raio ** 2)
area_cilindro = area_base + area_lateral
qtd_total_litros = area_cilindro / 3
qtd_latas = math.ceil(qtd_total_litros / 5)
custo = qtd_latas * 50

print(f'Área Lateral: {area_lateral}')
print(f'Área Base: {area_base}')
print(f'Área Cilindro: {area_cilindro}')
print(f'Quantidade Total de Litros: {qtd_total_litros}')
print(f'Quantidade de Latas: {qtd_latas}')

print((f'O custo total da atividade será de R${custo:.2f}.'))

