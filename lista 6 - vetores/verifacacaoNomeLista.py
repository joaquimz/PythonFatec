# 6 - Verifique se um nome digitado pelo usuário está em uma lista de nomes.

nomes = ["Ana", "Gabriel", "Carlos", "Diana","Du Lopes","Joao", "Joaquim", "Sara", "Pamonha", "Augusto"]
user_nome = input("Digite um nome para verificar se esta na lista: ")
achou = False

for verify in nomes:
    if verify.lower() == user_nome.lower():
        achou = True
        break
if achou == True:
    print(f"{user_nome} esta na lista! ")
else:
    print(f"{user_nome} não esta na lista!")