# 3 - Crie uma lista com 10 números e mostre apenas os números pares.
import random

numero = random.choices(range(1, 51), k=10)
lista = []
for item in numero:
    if item % 2 == 0:
     lista.append(item)
print(lista)