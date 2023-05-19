print("Vamos medir seu índice de massa corporal: ")
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso e o seu imc é: ", imc)
elif imc > 18.5 and imc < 25:
    print("Você está com o peso normal e o seu imc é: ", imc)
elif imc > 25 and imc < 30:
    print("Você está acima do peso e o seu imc é: ", imc)
elif imc > 30:
    print("Você está com obesidadee o seu imc é: ", imc)