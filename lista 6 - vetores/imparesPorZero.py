# 12 - Substitua todos os números ímpares de uma lista por zero.

lista = []
for i in range(1,50):
    if i % 2 == 0:
     lista.append(i)
    else:
        lista.append(0)

print(lista)
