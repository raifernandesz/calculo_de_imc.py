nome_do_paciente = input("escreva nome do paciente")
peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))


imc = peso / (altura*altura)


if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("peso normal")
elif imc >=25.0 and imc <= 29.9:
     print("sobrepeso")
elif imc >= 30.0 and imc <=34.9:
    print("Obesidade Grau I")
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade Grau II")
else: 
     print("Obesidade Grau III mórbida")


