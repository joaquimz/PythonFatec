# 17 - Faça uma função que recebe uma lista de números e retorna uma nova lista com o fatorial de cada número.
import math

lista_numeros = []
lista_fatorial = []

while True:
    num = int(input("Digite um número (ou 0 para parar): "))
    if num == 0:
        break
    lista_numeros.append(num)
for numero in lista_numeros:
    fatorial = math.factorial(numero)
    lista_fatorial.append(fatorial)
print(f"---Numeros digitados: {lista_numeros}---")
print(f"--Numeros fatorial: {lista_fatorial}--")
