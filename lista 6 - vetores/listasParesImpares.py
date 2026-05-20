# 7 - Faça um programa que leia 10 números e armazene em duas listas: uma com pares e outra com ímpares.

pares = []
impares = []
for i in range(1,11):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'{pares} numeros pares!')
print(f'{impares} numeros impares!')
