# 2 - Peça ao usuário para digitar 5 nomes e armazene-os em uma lista. Depois, exiba os nomes um por um.

lista = []
for i in range(5):
    nomes = input("Digite um nome para a lista: ")
    lista.append(nomes)
print(lista)
