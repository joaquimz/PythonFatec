#Solicite ao usuário um número e verifique se ele é par ou ímpar.
# Se o número for par, divida-o por 2 e exiba o resultado. Se o número for ímpar, multiplique-o por 3 e exiba o resultado.

numero = int(input("Digite um numero:"))

if numero % 2 == 0:
    divisao = numero / 2
    print(f"O número é par. O resultado da divisão por 2 é:{divisao}.")
else:
    multiplicacao = numero * 3
    print(f" O número é ímpar. O resultado da multiplicação por 3 é:{multiplicacao}")