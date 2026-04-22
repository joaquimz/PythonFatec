#Doação de sangue: idade entre 18 e 65 e peso >50kg.

idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

if idade >= 18 and idade <= 65 and peso > 50:
    print("Aprovado")
else:
    print("Reprovado")
