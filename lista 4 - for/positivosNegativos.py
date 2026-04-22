#Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero.

positivo = 0
negativo = 0
zeros = 0

for i in range (10):
    num = int(input(f"Digite o {i+1} numero: "))

    if num ==0:
        zeros += 1

    elif num < 0:
       negativo += 1

    else:
        positivo += 1

print(f"Positivos: {positivo}")
print(f"Negativos: {negativo}")
print(f"Zeros: {zeros}")
