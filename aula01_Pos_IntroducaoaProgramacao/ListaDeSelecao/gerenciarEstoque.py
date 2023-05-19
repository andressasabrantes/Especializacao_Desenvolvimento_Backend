qtd_minima = int(input("Informe a quantidade mínima que tem no estoque: "))
qtd_maxima = int(input("Informe a quantidade máxima que tem no estoque: "))
qtd_real = int(input("Informe a quantidade real que tem no estoque: "))

qtd_media = (qtd_maxima + qtd_minima) / 2

if qtd_real < qtd_media:
    print("Há necessidade de compra de mais produtos.")
elif qtd_real > qtd_media:
    print("Não há necessidade de adquirir novos produtos.")
elif qtd_real == qtd_media:
    print("Haverá necessidade da aquisição de novos produtos em breve.")

