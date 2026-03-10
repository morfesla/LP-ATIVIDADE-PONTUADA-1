import os

os.system("cls")

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A ou G): ")

if tipo == "A":
    preco = 3.79
    
    if litros <= 25:
        desconto = 0.02
    else:
        desconto = 0.04

elif tipo == "G":
    preco = 6.59
    
    if litros <= 25:
        desconto = 0.03
    else:
        desconto = 0.05

valor = litros * preco
valor_final = valor - (valor * desconto)

print("Valor a pagar:", valor_final)