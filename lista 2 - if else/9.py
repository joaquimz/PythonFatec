#Solicite o preço de um produto e aplique um desconto de 10% se o preço for maior que R$ 100. Exiba o valor final.

preco=float(input("Qual o preço do produto:"))
desconto= preco*0.10
final=preco-desconto
if preco>=100:
    print(f"O preço desse produto com o desconto e de {final} reais")
else:
    print(f"O produto custa {preco} reais")
