quantidade_maca = float(input("Informe quantas maçãs você deseja comprar: "));
valor_maca = 1.37;

if quantidade_maca < 12:
  valor_total = valor_maca * quantidade_maca
else:
    valor_maca = 1.24
    valor_total = valor_maca * quantidade_maca

print("o valor total das maçãs é de:", valor_total)