# 10 - Faça um programa que leia números do usuário até que ele digite 0. Depois, mostre a lista e a soma dos números.

lista_numeros = []

while True:
    numero = float(input(f'Digite um numero e digite (0) para somar toda a lista e parar o programa: '))
    lista_numeros.append(numero)
    if numero == 0:
        print(f'A soma de todos os numeros da lista foi de {sum(lista_numeros)}!')
        break


