import os 

os.system("cls")

nome = input("Digite o nome: ")
sexo = input("Digite seu sexo f/m: ")
estado_civil = input("Digite seu estado civil: ")

if sexo == "f" and estado_civil.upper() =="CASADA":
    anos = int(input("quantos anos de casada?: "))
else:
    anos = None
print("\n----DADOS--------")
print("NOME: ",nome)
print("Sexo:",sexo)
print("Estado civil: ",estado_civil)

if anos != None:
    print("Tempo de casada: ", anos,"anos")
