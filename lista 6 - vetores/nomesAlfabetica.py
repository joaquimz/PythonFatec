# 8 - Leia uma lista de 5 nomes e mostre a lista em ordem alfabética.

lista_nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
lista_nomes.sort()
for nome in lista_nomes:
    print(nome)
