#Peça ao usuário para digitar 5 números e exiba o maior e o menor deles.

maior = 0
menor = 0

for i in range(5):
   num = float(input(f"Digite o {i+1} numero: "))

   if i == 0:
     maior = num
     menor = num
else:

    if num > maior:
      maior = num

    if num < menor:
         menor = num

print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")




