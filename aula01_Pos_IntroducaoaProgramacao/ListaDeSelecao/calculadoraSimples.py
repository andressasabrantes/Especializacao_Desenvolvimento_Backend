operacao = input("Qual operação você deseja realizar? "
                 "Adição: + |"
                 "Subtração: - |"
                 "Multiplicação: * |"
                 "Divisão: / |"
                 "Potenciação: **| : ")
primeiro_valor = float(input("Digite o primeiro número: "))
segundo_valor = float(input("Digite o segundo número: "))

if operacao == '+':
    print("o resultado da operação é:", primeiro_valor + segundo_valor)
elif operacao == '-':
    print("o resultado da operação é:", primeiro_valor - segundo_valor)
elif operacao == '*':
    print("o resultado da operação é:", primeiro_valor * segundo_valor)
elif operacao == '/':
    print("o resultado da operação é:", primeiro_valor / segundo_valor)
elif operacao == '**':
    print("o resultado da operação é:", primeiro_valor ** segundo_valor)