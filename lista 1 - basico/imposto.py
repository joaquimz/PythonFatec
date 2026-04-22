#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

cf=float(input("Qual o custo de fabrica do veiculo?")) #cf é Custo de fabrica.
pd= cf*0.28 #pd é a percentagem do distribuidor 28%.
impostos= cf*0.45 # os impostos de 45%.
valorfinal= cf+pd+impostos
print(f"O custo do veiculo para o consumidor final sera de {valorfinal} reais")
