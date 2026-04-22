#Peça a quantidade de kWh consumidos e o valor por kWh, depois calcule o valor da conta de energia.

kwh=float(input("Digite a quantidade de kWh consumidos:"))
valor=float(input("Digite o valor do kWh na sua cidade:"))
conta= kwh*valor
print(f"O valor da sua conta de luz e de {conta} reais")
