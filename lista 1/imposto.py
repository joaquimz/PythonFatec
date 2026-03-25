cf=float(input("Qual o custo de fabrica do veiculo?")) #cf é Custo de fabrica.
pd= cf*0.28 #pd é a percentagem do distribuidor 28%.
impostos= cf*0.45 # os impostos de 45%.
valorfinal= cf+pd+impostos
print(f"O custo do veiculo para o consumidor final sera de {valorfinal} reais")
