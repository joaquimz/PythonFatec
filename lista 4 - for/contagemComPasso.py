#Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

for numero in range(n1, n2, n3):
    print(numero)