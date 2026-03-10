import os

os.system("cls")

morango = float(input("Digite a quantidade de morango (KG): "))
maca = float(input("Digite a quantidade de maçã (KG): "))

if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.50

if maca <= 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

total = preco_morango + preco_maca
peso_total = morango + maca

if peso_total >=10 or total >15:
    total = total * 0.9
print("Valor total a pagar: R$", total)    
