import os

os.system("cls")

print("\n----Tabela de preços------")
print("Verde = R$10")
print("Azul = R$20")
print("Amarelo = R$30")
print("Vermelho = R$40")

cor = input("Digite a cor do CD: ").lower()

if cor == "verde":
    preco = 10
elif cor == "azul":
    preco = 20
elif cor == "amarelo":
    preco = 30
elif cor == "vermelho":
    preco = 40
else:
    preco = 0
    print("Cor inválida")

if preco != 0:
    print("Preço do CD: R$", preco)