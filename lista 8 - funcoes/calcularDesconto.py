#Crie uma função calcular_desconto(valor, percentual=10) que aplique um desconto percentual ao valor.

def calcular_desconto(valor, percentual=10):
    desconto = valor * (percentual / 100)
    valor_final = valor - desconto
    return valor_final

valor = float(input("Digite o valor da compra: "))
print(calcular_desconto(valor))