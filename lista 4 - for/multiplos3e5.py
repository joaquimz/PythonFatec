#Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5.

multiplos = 0

n = int(input("Digite um numero:"))

for i in range(1,n):
    if i % 15 == 0 and i % 5 == 0:
     multiplos += 1

print(f"Entre 1 e {n} tem {multiplos} multiplos de 3 e 5.")