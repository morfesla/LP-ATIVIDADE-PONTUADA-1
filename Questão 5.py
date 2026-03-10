import os

os.system("cls")

operecao = input("Digite a operação:  (+, -, *, /): ")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if operecao == "+":
    resultado = A + B
elif operecao == "-":
    resultado = A - B
elif operecao == "*":
    resultado = A * B
elif operecao == "/":
    resultado = A / B
else:
    print("Operação inválida")
print("Resultado:", resultado)