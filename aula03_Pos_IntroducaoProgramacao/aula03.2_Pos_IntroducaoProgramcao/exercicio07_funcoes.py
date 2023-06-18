def calculadora(n1, n2):
    resultado_soma = n1 + n2
    resultado_sub = n1 - n2
    resultado_mult = n1 * n2
    resultado_div = n1 / n2

    return resultado_soma, resultado_sub, resultado_mult, resultado_div

soma, subtracao, mulltiplicacao, divisao = calculadora(10, 20)

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {mulltiplicacao}')
print(f'Divisão: {divisao}')
