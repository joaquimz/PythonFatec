#Crie um programa que solicite ao usuário um número e informe se ele é primo ou não. Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

numero = int(input("Digite um numero inteiro:"))
primo = 0

for i in range(1, numero, +1):

    if numero % i == 0:
        primo += 1

if primo == 2:
    print(f"{numero} Não e Primo")
else:
    print(f"{numero} é Primo")