#Crie um menu com funções para: Cadastrar nomes, Listar nomes e Sair do programa.

def menu_nomes():
  lista_nomes = []
  while True:
    print("---MENU---")
    print("[1] CADASTRAR NOMES")
    print("[2] LISTAR NOMES")
    print("[3] SAIR")
    user = input("Escolha uma opção:")
    if user == "1":
        add_nome = input("Digite um nome para cadastrar: ")
        lista_nomes.append(add_nome)
    elif user == "2":
        print(lista_nomes)
    elif user == "3":
        print("Saindo...")
        break
    else:
        print("Opção invalida. Tente novamente.")

menu_nomes()