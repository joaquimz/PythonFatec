#Crie uma função converter_para_fahrenheit(celsius) que converta graus Celsius para Fahrenheit.

def converter_para_fahrenheit(celsius):
    return celsius * 1.8 + 32


graus = int(input("Digite a quantidade de graus celsius para converter para fahrenheit: "))
print(converter_para_fahrenheit(graus))