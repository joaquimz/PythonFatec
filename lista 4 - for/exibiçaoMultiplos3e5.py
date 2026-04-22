#Peça ao usuário um número N e exiba todos os números de 1 até N que são múltiplos de 3 e 5.

resultados = []

n = int(input("Digite um numero:"))
for i in range(1, n):
     if i % 15 == 0 and i % 5 == 0:
      resultados.append(i)

print(f"Os múltiplos de 3 e 5 entre 1 e {n} são: {resultados}")

