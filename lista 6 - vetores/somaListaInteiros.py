# 4 - Some todos os elementos de uma lista de inteiros digitados pelo usuário.

lista = []
for i in range(100):
    numero = int(input('Digite um numero ou (0) para mostrar o resultado: '))
    if numero == 0:
        break
    else:
      lista.append(numero)
print(sum(lista))