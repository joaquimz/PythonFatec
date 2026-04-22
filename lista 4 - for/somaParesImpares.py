#Peça um número ao usuário e some separadamente os pares e os ímpares de 1 até esse número.

numero = int(input("Digite um numero:"))

soma_pares = 0
soma_impar = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        soma_pares = soma_pares + i
    else:
        soma_impar = soma_impar + i

print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impar}")