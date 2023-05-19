saldo_conta = 0
valor_total = 0

deposito = input("Deseja realizar um depósito? S/N ")
if deposito == 's' or deposito == 'S':
    valor_deposito = float(input("Quanto você quer depositar? "))
    saldo_conta += valor_deposito

saque = float(input("Informe quanto você deseja sacar: "))

if saldo_conta - saque < 0:
    print(f"O saldo da conta é de {saldo_conta - saque} e está negativo! Você precisa de {abs(saldo_conta - saque)} para quitar o seu débito!")
elif saldo_conta - saque > 0:
    print(f"O saldo da conta é de {saldo_conta - saque} e está positivo! Não há débitos em sua conta!")
